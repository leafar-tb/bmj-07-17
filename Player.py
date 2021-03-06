import pygame
from pygame.locals import *
import GameState
from Sprite import HealthSprite
from Config import SCALE, PLAYER_HEALTH

class Player(HealthSprite):
    
    def __init__(self, position, size=SCALE):
        HealthSprite.__init__(self, "player_placeholder.png", position, size, PLAYER_HEALTH)
        GameState.player = self
        GameState.dynamics.add(self)
    
    def keydown(self, key):
        vector = None
        if key in (K_a, K_LEFT):
            vector = (-SCALE, 0)
        elif key in (K_w, K_UP):
            vector = (0, -SCALE)
        elif key in (K_d, K_RIGHT):
            vector = (SCALE, 0)
        elif key in (K_s, K_DOWN):
            vector = (0, SCALE)
        
        if vector is not None:
            self.moveBy(*vector)
