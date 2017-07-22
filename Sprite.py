#/usr/bin/python

import os, sys
import pygame
from pygame.locals import *

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image, position, size=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            os.path.join('resources', 'sprites', image)).convert()
        if size is not None:
            if type(size) is int or type(size) is float:
                size = size, size
            self.image = pygame.transform.scale(self.image, size)
        
        self.rect = self.image.get_rect(center=position)
        
    def moveBy(self, x, y):
        self.rect.x += x
        self.rect.y += y
