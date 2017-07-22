import pygame
from pygame.locals import *
import sys, os, math
from generation import genMaze
from Sprite import Sprite, HealthSprite
from Item import Item, HealItem
from Enemy import Enemy
import GameState
import UI
import random
from Player import Player
from Config import SCALE, MAPSIZE

pygame.init()
screen = pygame.display.set_mode((640, 480))

Player((0,0), SCALE)
UI.UIText.FONT = pygame.font.Font(None, 40)
UIGroup = pygame.sprite.Group()
UIGroup.add(
    UI.UIText(
        lambda: "Health: %s"%GameState.player.hp,
        {"topleft":(0,0)}))
UIGroup.add(
    UI.UIText(
        lambda: "Level: %s"%GameState.level,
        {"topright":screen.get_rect().topright}))
        
wallimg = pygame.image.load(
    os.path.join('resources', 'sprites', "wall.png")).convert()
wallimg = pygame.transform.scale(wallimg, (SCALE, SCALE))

def createLevel():
    GameState.clean()
    GameState.level += 1
    
    stairUp = Item("stairs_up.png", (SCALE, SCALE), GameState.triggerLoad)
    GameState.dynamics.add(stairUp)
    playerPos = None
    maze = genMaze(MAPSIZE+GameState.level)
    
    floors = sum(sum(maze.data))
    spawns = [lambda pos: HealItem(pos, 1) for _ in range(int(0.02*floors))]
    spawns += [lambda pos: Enemy("enemy_placeholder.png", pos) for _ in range(int(0.05*floors))]
    
    for x in range(maze.M+2):
        for y in range(maze.N+2):
            if not maze[x-1,y-1]:
                GameState.statics.add(Sprite(wallimg, (x*SCALE, y*SCALE)))
            elif playerPos is None:
                playerPos = x*SCALE, y*SCALE
            elif random.random() < .01 and x < maze.M/2 and y < maze.N:
                playerPos = x*SCALE, y*SCALE
            else:
                if random.random() < max(len(spawns)/floors, .05) and spawns:
                    i = random.randrange(len(spawns))
                    GameState.dynamics.add(spawns[i]((x*SCALE,y*SCALE)))
                    del spawns[i]
                floors -= 1
                stairUp.rect.x, stairUp.rect.y = x*SCALE, y*SCALE

    GameState.initBackground()    
    GameState.player.rect.topleft = playerPos

def handlePlayerInput():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif not GameState.gameOver and event.type == KEYDOWN:
            GameState.player.keydown(event.key)

while not GameState.gameOver:
    if GameState.loadNextLevel:
        createLevel()
    handlePlayerInput()
    
    # camera follows player
    GameState.cameraPos = GameState.player.rect.left-screen.get_rect().width//2, \
        GameState.player.rect.top-screen.get_rect().height//2
    
    GameState.dynamics.update()
    GameState.draw(screen)
    
    UIGroup.update()
    UIGroup.draw(screen)
    
    pygame.display.update()
    pygame.time.delay(100)
    

while 1:
    handlePlayerInput()
    UIGroup.add( UI.UIText(
        lambda: "Game Over",
        {"center":screen.get_rect().center},
        (255,0,0)) )
    UIGroup.update()
    UIGroup.draw(screen)
    
    pygame.display.update()
    
