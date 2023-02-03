import pygame
from functions import *
from classes import * 
pygame.init()

Screen = [1920, 1080]

#älä muuta, kaikki kusee sitte
#frames per second

POSSIBLE_ACTIONS = {"Up": moveUp(), "Down": moveDown(), "Left": moveLeft(), "Right": moveRight(), "Jump": jump(), "Quit": ()}
Player = ENTITY(0.0, 0.0, 32, 60, 0.67, 0.0, 0.0)

RUNNING = True

#main loop

def main():
    Window = pygame.display.set_mode((Screen[0], Screen[1]))
    PressedKeys = []
    clock = pygame.time.Clock()
    MAX_FPS = 30
    
    print(Player)
    while(RUNNING):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        if(pygame.key.get_focused): #only do main loop while window focused
            PressedKeys = getInput() #actions to perform
            actionDoer(PressedKeys)

        else:
            pass


        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
