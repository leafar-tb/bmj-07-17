from Sprite import Sprite
import random

class Enemy(Sprite):
    
    def __init__(self, image, size):
        position = (random.randrange(0, 10) * size, random.randrange(0, 10) * size)
        
        Sprite.__init__(self, image, position, size)
        
        self.hp = 3
        self.timeSinceRoam = 0
        
    
    
    def roam(self, SCALE, colliders):
        self.timeSinceRoam += 1
        if self.timeSinceRoam > 3:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))), colliders=colliders)
            self.timeSinceRoam = 0
