#/usr/bin/python

import os, sys
import pygame
from pygame.locals import *

statics = pygame.sprite.Group()
moving = pygame.sprite.Group()

cameraPos = [0,0]
def toView(pos):
    return pos[0]-cameraPos[0], pos[1]-cameraPos[1]
def fromView(pos):
    return pos[0]+cameraPos[0], pos[1]+cameraPos[1]
