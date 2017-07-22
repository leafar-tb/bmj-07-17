import pygame
from pygame.locals import *
import sys, os
from generation import genMaze
from Sprite import Sprite
from Enemy import Enemy
import GameState
import UI
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

SCALE = 20
MAZESIZE = 40

wallimg = pygame.image.load(
    os.path.join('resources', 'sprites', "wall.png")).convert()
wallimg = pygame.transform.scale(wallimg, (SCALE, SCALE))

stairUp = Sprite("stairs_up.png", (SCALE, SCALE), SCALE)
GameState.stairs.add(stairUp)
maze = genMaze(MAZESIZE)
playerPos = None
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

player = Sprite("player_placeholder.png", playerPos, SCALE)
GameState.moving.add(player)

enemies = pygame.sprite.Group()
for i in range(3):
    enemies.add(Enemy("enemy_placeholder.png", SCALE, MAZESIZE))
GameState.moving.add(*enemies)

UI.UIText.FONT = pygame.font.Font(None, 40)
UIGroup = pygame.sprite.Group()
UIGroup.add(
    UI.UIText(
        lambda: "%s,%s"%player.rect.center,
        {"topleft":(0,0)}))

def handlePlayerInput():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif event.type == KEYDOWN and event.key in (K_a, K_w, K_d, K_s, K_UP, K_DOWN, K_LEFT, K_RIGHT):
            movePlayer(event.key)

def movePlayer(key):
    vector = (-SCALE, 0)
    if key in (K_w, K_UP):
        vector = (0, -SCALE)
    elif key in (K_d, K_RIGHT):
        vector = (SCALE, 0)
    elif key in (K_s, K_DOWN):
        vector = (0, SCALE)
            
    player.moveBy(*vector, colliders=walls)

while 1:
    handlePlayerInput()
    
    # camera follows player
    GameState.cameraPos = player.rect.left-screen.get_rect().width//2, \
        player.rect.top-screen.get_rect().height//2
            
    GameState.draw(screen)
    for e in enemies:
        e.roam(SCALE, walls)
    
    UIGroup.update()
    UIGroup.draw(screen)
    
    pygame.display.update()
    pygame.time.delay(100)
