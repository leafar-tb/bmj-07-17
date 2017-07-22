import pygame
from pygame.locals import *
import sys
from generation import genMaze
from Sprite import Sprite
import GameState

pygame.init()

screen = pygame.display.set_mode((640, 480))

maze = genMaze(20)
walls = pygame.sprite.Group()
floors = pygame.sprite.Group()
SCALE = 20

player = pygame.sprite.Group(Sprite("player_placeholder.png", (0, 0), SCALE))
for x in range(maze.M):
    for y in range(maze.N):
        if not maze[x,y]:
            walls.add(Sprite("wall_placeholder.png", (x*SCALE+SCALE/2, y*SCALE+SCALE/2), SCALE))

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
            
    for p in player:
        p.moveBy(*vector, walls)

while 1:
    handlePlayerInput()
    
    screen.fill((0,0,0))
    for sprite in walls:
        sprite.draw(screen)
    player.draw(pygame.display.get_surface())
    
    #GameState.cameraPos[0] += 1
    pygame.display.update()
    pygame.time.delay(100)

