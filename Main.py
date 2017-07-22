import pygame
from pygame.locals import *
import sys, os
from generation import genMaze
from Sprite import Sprite
from Enemy import Enemy
import GameState
import UI

pygame.init()
screen = pygame.display.set_mode((640, 480))

SCALE = 20

player = Sprite("player_placeholder.png", (SCALE, SCALE), SCALE)
GameState.moving.add(player)

wallimg = pygame.image.load(
    os.path.join('resources', 'sprites', "wall.png")).convert()
wallimg = pygame.transform.scale(wallimg, (SCALE, SCALE))

maze = genMaze(40)
walls = pygame.sprite.Group()
for x in range(maze.M+2):
    for y in range(maze.N+2):
        if not maze[x-1,y-1]:
            walls.add(Sprite(wallimg, (x*SCALE, y*SCALE)))

GameState.statics.add(*walls)
GameState.initBackground()

enemies = pygame.sprite.Group()
for i in range(3):
    enemies.add(Enemy("enemy_placeholder.png", SCALE))
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
        elif event.type == KEYDOWN and event.key in (K_a, K_w, K_d, K_s):
            movePlayer(event.key)

def movePlayer(key):
    vector = (-SCALE, 0)
    if key == K_w:
        vector = (0, -SCALE)
    elif key == K_d:
        vector = (SCALE, 0)
    elif key == K_s:
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
