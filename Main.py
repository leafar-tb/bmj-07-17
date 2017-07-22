import pygame
from pygame.locals import *
import sys
from generation import genMaze
from Sprite import Sprite
import GameState

pygame.init()
screen = pygame.display.set_mode((640, 480))

SCALE = 20

player = Sprite("player_placeholder.png", (SCALE, SCALE), SCALE)
GameState.moving.add(player)

maze = genMaze(20)
walls = pygame.sprite.Group()
floors = pygame.sprite.Group()
for x in range(maze.M+2):
    for y in range(maze.N+2):
        if not maze[x-1,y-1]:
            walls.add(Sprite("wall_placeholder.png", (x*SCALE, y*SCALE), SCALE))

GameState.statics.add(*walls)
GameState.initBackground()

def handlePlayerInput():
    for event in pygame.event.get():
        if event.type == QUIT:
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
    pygame.display.update()
    pygame.time.delay(100)
