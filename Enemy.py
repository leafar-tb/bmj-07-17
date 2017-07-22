from Sprite import Sprite
import random

class Enemy(Sprite):
    
    def __init__(self, image, size, positionRange):
        position = (random.randrange(1, positionRange) * size, random.randrange(1, positionRange) * size)
        
        Sprite.__init__(self, image, position, size)
        
        self.hp = 3
        self.timeSinceRoam = 0
        

    
    def roam(self, SCALE, colliders):
        self.timeSinceRoam += 1
        if self.timeSinceRoam > 10:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))), colliders=colliders)
            self.timeSinceRoam = 0
