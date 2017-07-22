import pygame
from Sprite import HealthSprite
from Config import SCALE, ENEMY_MOVE_INTERVAL
import random
import GameState

class Enemy(HealthSprite):
    
    def __init__(self, image, position, size=SCALE):
        HealthSprite.__init__(self, image, position, size, 3)
        self.lastRoam = 0

    def update(self):
        if self.rect.colliderect(GameState.player.rect):
            GameState.player.hit(1)
        self.roam()
    
    def roam(self):
        if pygame.time.get_ticks()-self.lastRoam >= ENEMY_MOVE_INTERVAL:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))))
            self.lastRoam = pygame.time.get_ticks()
