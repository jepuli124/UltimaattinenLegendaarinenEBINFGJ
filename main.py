import pygame
from functions import *
from classes import * 
from math import sqrt, ceil, floor
pygame.init()

Screen = [1920, 1080]

#main loop
def main():
    Window = pygame.display.set_mode((Screen[0], Screen[1]))
    PressedKeys = []
    Gravity = 1
    clock = pygame.time.Clock()
    MAX_FPS = 30
    Player = ENTITY(0.0, 0.0, 32, 60, 4, 0.0, 0.0)

    CollisionDetectionRange = ceil((sqrt(Player.characterHeightX^2 + Player.characterHeightY^2) + Player.maxVelocity) / 32)

    NewStage = True
    CurrentStage = "testStage.txt"

    while(RUNNING):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        if(pygame.key.get_focused): #only do main loop while window focused
            if(NewStage is True): #update level if flagged so
                level = readLevelFromFile(CurrentStage)
                NewStage = False
            PressedKeys = getInput() #actions to perform
            Player = actionDoer(PressedKeys, Player)
            if(Player.grounded is False):
                Player.VelocityY += Gravity
            Player = updatePlayerPos(Player, level, CollisionDetectionRange)
        else:
            pass


        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
