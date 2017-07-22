from Sprite import HealthSprite
import random
import GameState

class Enemy(HealthSprite):
    
    def __init__(self, image, size, positionRange):
        position = (random.randrange(1, positionRange) * size, random.randrange(1, positionRange) * size)
        
        HealthSprite.__init__(self, image, position, size, 3)
        self.timeSinceRoam = 0
        
    def update(self):
        if self.rect.colliderect(GameState.player.rect):
            GameState.player.hit(1);
    
    def roam(self, SCALE, colliders):
        self.timeSinceRoam += 1
        if self.timeSinceRoam > 10:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))), colliders=colliders)
            self.timeSinceRoam = 0
