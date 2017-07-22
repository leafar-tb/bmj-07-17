#/usr/bin/python

import os, sys
import pygame
from pygame.locals import *
import GameState

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image, position, size=None):
        pygame.sprite.Sprite.__init__(self)
        
        if type(image) == str:
            self.image = pygame.image.load(
                os.path.join('resources', 'sprites', image)).convert()
        else:
            self.image = image
        
        if size is not None:
            if type(size) is int or type(size) is float:
                size = size, size
            self.image = pygame.transform.scale(self.image, size)
        
        self.rect = self.image.get_rect(topleft=position)
        
    def moveBy(self, x, y, colliders=()):
        destination = (self.rect.x + x, self.rect.y + y)
        
        for c in colliders:
            if c.rect.collidepoint(destination):
                return False
                
        self.rect.x, self.rect.y = destination
        return True
    
    def draw(self, surface):
        surface.blit(self.image, GameState.toView(self.rect.topleft))

class HealthSprite(Sprite):
    
    def __init__(self, image, position, size=None, health=1):
        Sprite.__init__(self, image, position, size)
        self.maxHp = health
        self.hp = health
        self.lasthit = 0
    
    def heal(self, amount):
        self.hp = min(self.maxHp, self.hp+amount)
    
    def hit(self, damage):
        #1s i-frame after being hit
        if pygame.time.get_ticks() - self.lasthit < 1000:
            return
        self.hp -= damage
        self.lasthit = pygame.time.get_ticks()
        if self.hp <= 0:
            self.kill()
            if self is GameState.player:
                GameState.gameOver = True
