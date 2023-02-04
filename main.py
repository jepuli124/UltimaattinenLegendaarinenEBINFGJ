import pygame
from functions import *
from classes import * 

#main loop
def main():
    Window = pygame.display.set_mode((Screen[0], Screen[1]))
    clock = pygame.time.Clock()
    MAX_FPS = 30

    while(RUNNING):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
