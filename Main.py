import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	pygame.display.update()
	pygame.time.delay(100)
