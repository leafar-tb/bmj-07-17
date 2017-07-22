import os, sys
import pygame
from pygame.locals import *
import GameState
from Config import SCALE

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image, position, size=SCALE):
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
        self.blocksMovement = True
        
    def moveBy(self, x, y):
        destination = (self.rect.x + x, self.rect.y + y)
        def collideany(group):
            for s in group.sprites():
                if s.blocksMovement and s.rect.collidepoint(destination):
                    return True
            return False
        
        if collideany(GameState.statics) or collideany(GameState.dynamics):
            return False
        
        self.rect.x, self.rect.y = destination
        return True
    
    def draw(self, surface):
        surface.blit(self.image, GameState.toView(self.rect.topleft))

class HealthSprite(Sprite):
    
    def __init__(self, image, position, size=SCALE, health=1):
        Sprite.__init__(self, image, position, size)
        self.maxHp = health
        self.hp = health
        self.lasthit = 0
        self.blocksMovement = False
    
    def heal(self, amount):
        hpBefore = self.hp
        self.hp = min(self.maxHp, self.hp+amount)
        return self.hp != hpBefore
    
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
