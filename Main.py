import pygame
from pygame.locals import *
import sys
from generation import genMaze
from Sprite import Sprite

pygame.init()

screen = pygame.display.set_mode((640, 480))

maze = genMaze(20)
walls = pygame.sprite.Group()
floors = pygame.sprite.Group()
SCALE = 20
for x in range(maze.M):
    for y in range(maze.N):
        if not maze[x,y]:
            walls.add(Sprite("wall_placeholder.png", (x*SCALE+SCALE/2, y*SCALE+SCALE/2), SCALE))

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    walls.draw(pygame.display.get_surface())
    pygame.display.update()
    pygame.time.delay(100)
