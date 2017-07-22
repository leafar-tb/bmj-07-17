import pygame
import GameState
from Sprite import Sprite
from Config import SCALE

class Item(Sprite):
    
    def __init__(self, image, position, function, size=SCALE):
        Sprite.__init__(self, image, position, size)
        self.function = function
        self.blocksMovement = False
    
    def update(self):
        if self.rect.colliderect(GameState.player.rect):
            if self.function():
                self.kill()

healimg = pygame.surface.Surface((10,10))
healimg.fill((255,0,255))
def _healPlayer(amount):
    GameState.player.heal(amount)
    return True

def HealItem(position, amount, size):
    return Item(healimg, position, lambda: _healPlayer(amount), size=size)
