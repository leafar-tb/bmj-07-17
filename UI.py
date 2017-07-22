import pygame
from pygame.locals import *

class UIText(pygame.sprite.Sprite):
    
    FONT = None
    
    def __init__(self, textGetter, positioning, color=(255,255,255)):
        pygame.sprite.Sprite.__init__(self)
        self.text = textGetter
        self.positioning = positioning
        self.lasttext = None
        self.color = color
        
        self.update()
    
    def update(self):
        txt = self.text()
        if txt != self.lasttext:
            self.image = UIText.FONT.render(txt, True, self.color)
            self.rect = self.image.get_rect(**self.positioning)
