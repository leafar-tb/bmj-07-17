import os, sys
import pygame
from pygame.locals import *

statics = pygame.sprite.Group()
dynamics = pygame.sprite.Group()
player = None
gameOver = False
loadNextLevel = True

cameraPos = [0,0]

def triggerLoad():
    global loadNextLevel
    loadNextLevel = True

def clean():
    statics.empty()
    dynamics.empty()
    dynamics.add(player)
    global loadNextLevel
    loadNextLevel = False

def initBackground():
    global bgRect, background, cameraPos
    bgRect = statics.sprites()[0].rect.unionall(list(map(lambda s: s.rect, statics)))
    background = pygame.surface.Surface(bgRect.size)
    
    oldCam = cameraPos
    cameraPos = bgRect.topleft # modify for drawing
    for s in statics:
        s.draw(background)
    cameraPos = oldCam # reset
    
def draw(screen):
    screen.fill((0, 0, 0))
    screen.blit(background, toView(bgRect.topleft))
    for s in dynamics:
        s.draw(screen)
    
def toView(pos):
    return pos[0]-cameraPos[0], pos[1]-cameraPos[1]
def fromView(pos):
    return pos[0]+cameraPos[0], pos[1]+cameraPos[1]
