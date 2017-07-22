import pygame
import GameState
from Sprite import Sprite

class Item(Sprite):
    
    def __init__(self, image, position, function, size=None):
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

def HealItem(position, amount, size):
    return Item(healimg, position, lambda: _healPlayer(amount), size=size)
