import pygame
from Sprite import HealthSprite
import random
import GameState

class Enemy(HealthSprite):
    
    def __init__(self, image, size, positionRange):
        position = (random.randrange(1, positionRange) * size, random.randrange(1, positionRange) * size)
        
        HealthSprite.__init__(self, image, position, size, 3)
        self.lastRoam = 0

    def update(self):
        if self.rect.colliderect(GameState.player.rect):
            GameState.player.hit(1)
        self.roam()
    
    def roam(self):
        SCALE = self.rect.width
        self.lastRoam += 1
        if pygame.time.get_ticks()-self.lastRoam >= 1000:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))))
            self.timeSinceRoam = pygame.time.get_ticks()
