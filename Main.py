import pygame
from pygame.locals import *
import sys, os
from generation import genMaze
from Sprite import Sprite, HealthSprite
from Enemy import Enemy
import GameState
import UI
import random

SCALE   = 20
MAPSIZE = 10

pygame.init()
screen = pygame.display.set_mode((640, 480))

wallimg = pygame.image.load(
    os.path.join('resources', 'sprites', "wall.png")).convert()
wallimg = pygame.transform.scale(wallimg, (SCALE, SCALE))

stairUp = Sprite("stairs_up.png", (SCALE, SCALE), SCALE)
GameState.stairs.add(stairUp)
playerPos = None
maze = genMaze(MAPSIZE)
walls = pygame.sprite.Group()
for x in range(maze.M+2):
    for y in range(maze.N+2):
        if not maze[x-1,y-1]:
            walls.add(Sprite(wallimg, (x*SCALE, y*SCALE)))
        elif playerPos is None:
            playerPos = x*SCALE, y*SCALE
        elif random.random() < .01:
            playerPos = x*SCALE, y*SCALE
        else:
            stairUp.rect.x, stairUp.rect.y = x*SCALE, y*SCALE
            

GameState.statics.add(*walls)
GameState.initBackground()

GameState.player = HealthSprite("player_placeholder.png", playerPos, SCALE, 3)
GameState.dynamics.add(GameState.player)

enemies = pygame.sprite.Group()
for i in range(3):
    enemies.add(Enemy("enemy_placeholder.png", SCALE, MAPSIZE))
GameState.dynamics.add(*enemies)

UI.UIText.FONT = pygame.font.Font(None, 40)
UIGroup = pygame.sprite.Group()
UIGroup.add(
    UI.UIText(
        lambda: "Health: %s"%GameState.player.hp,
        {"topleft":(0,0)}))

def handlePlayerInput():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif not GameState.gameOver and event.type == KEYDOWN:
            movePlayer(event.key)

def movePlayer(key):
    vector = None
    if key in (K_a, K_LEFT):
        vector = (-SCALE, 0)
    elif key in (K_w, K_UP):
        vector = (0, -SCALE)
    elif key in (K_d, K_RIGHT):
        vector = (SCALE, 0)
    elif key in (K_s, K_DOWN):
        vector = (0, SCALE)
    
    if vector is not None:
        GameState.player.moveBy(*vector, colliders=walls)

while not GameState.gameOver:
    handlePlayerInput()
    
    # camera follows player
    GameState.cameraPos = GameState.player.rect.left-screen.get_rect().width//2, \
        GameState.player.rect.top-screen.get_rect().height//2
    
    GameState.dynamics.update()
    GameState.draw(screen)
    for e in enemies:
        e.roam(SCALE, walls)
    
    UIGroup.update()
    UIGroup.draw(screen)
    
    pygame.display.update()
    pygame.time.delay(100)

while 1:
    handlePlayerInput()
    UIGroup.add( UI.UIText(
        lambda: "Game Over",
        {"center":screen.get_rect().center},
        (255,0,0)) )
    UIGroup.update()
    UIGroup.draw(screen)
    
    pygame.display.update()
    
