from Sprite import HealthSprite
import random
import GameState

class Enemy(HealthSprite):
    
    def __init__(self, image, size):
        position = (random.randrange(0, 10) * size, random.randrange(0, 10) * size)
        
        HealthSprite.__init__(self, image, position, size, 3)
        self.timeSinceRoam = 0
    
    def update(self):
        if self.rect.colliderect(GameState.player.rect):
            GameState.player.hit(1);
    
    def roam(self, SCALE, colliders):
        self.timeSinceRoam += 1
        if self.timeSinceRoam > 3:
            self.moveBy(*random.choice(((-SCALE, 0), (0, -SCALE), (SCALE, 0), (0, SCALE))), colliders=colliders)
            self.timeSinceRoam = 0
