#/usr/bin/python

import os, sys
import pygame
from pygame.locals import *

statics = pygame.sprite.Group()
moving = pygame.sprite.Group()

cameraPos = [0,0]

def initBackground():
    global bgRect, background
    bgRect = statics.sprites()[0].rect.unionall(list(map(lambda s: s.rect, statics)))
    background = pygame.surface.Surface(bgRect.size)
    
    cameraPos = bgRect.topleft # modify for drawing
    for s in statics:
        s.draw(background)
    cameraPos = [0,0] # reset
    
def draw(screen):
    screen.fill((0,0,0))
    screen.blit(background, toView(bgRect.topleft))
    for s in moving:
        s.draw(screen)
    
def toView(pos):
    return pos[0]-cameraPos[0], pos[1]-cameraPos[1]
def fromView(pos):
    return pos[0]+cameraPos[0], pos[1]+cameraPos[1]
