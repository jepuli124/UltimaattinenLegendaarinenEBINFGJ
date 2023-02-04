import pygame
from functions import *
from classes import * 
from math import sqrt, ceil, floor

pygame.init()

# load Pictures:

leaf1 = pygame.image.load("./textures/leaf1.png")
leaf2 = pygame.image.load("./textures/leaf2.png")
leaf3 = pygame.image.load("./textures/leaf3.png")
leaf4 = pygame.image.load("./textures/leaf4.png")
leaf5 = pygame.image.load("./textures/leaf5.png")
Axe = pygame.image.load("./textures/Axe.png")
cha = pygame.image.load("./textures/päähahmo.png")

startB = pygame.image.load("./textures/tausta.png")
perhonen1 = pygame.image.load("./textures/perhonen1.png")
perhonen2 = pygame.image.load("./textures/perhonen2.png")
perhonen3 = pygame.image.load("./textures/perhonen3.png")
head = pygame.image.load("./textures/GAME JAM head.png")
head2 = pygame.image.load("./textures/GAME JAM head anime.png")


Screen = [1920, 1080]
Window = pygame.display.set_mode((Screen[0], Screen[1]), )
pygame.display.set_caption("MOST ULTIMATE LEGEDARY GAME THING EVER")
font = pygame.font.Font('freesansbold.ttf', 150)
starttext = font.render("Loading", True, (255, 255, 255))
Window.blit(starttext, ((Screen[0] / 2) - 300, (Screen[1] / 2) - 75))
pygame.display.flip()

# Loading Loop


def startloop():
    clocks = pygame.time.Clock()
    MAX_FPS = 30
    space = pygame.key.get_pressed()
    ListOfMBG = []
    ListOfSBG = [perhonen1, perhonen2, perhonen3, head, head2]
    ListOfDraw = [ListOfMBG]
    while not space[pygame.K_SPACE]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        space = pygame.key.get_pressed()
        ListOfMBG = MBGCheckListWP(ListOfMBG, ListOfSBG)
        Window.blit(startB, (0, 0))  # BG
        drawWhole(ListOfDraw, Window)
        pygame.display.flip()
        clocks.tick(MAX_FPS)


#main loop
def main():
    RUNNING = True
    clock = pygame.time.Clock()
    MAX_FPS = 30
    NewStage = True
    CurrentStage = "testLevel.txt"
    ListOfEntities = []
    ListOfSolid = []
    ListOfMBG = []
    ListOfSBG = [leaf1, leaf2, leaf3, leaf4, leaf5]
    ListOfDraw = [ListOfSolid, ListOfEntities, ListOfMBG]
    createPlayer(ListOfEntities, cha)


    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break

        #if(NewStage is True): #update level if flagged so
        #    level = readLevelFromFile(CurrentStage)
        #    if level == "exit":
        #        RUNNING = False
        #        break
        #    NewStage = False
        if getInput(ListOfEntities[0]) == 1: #actions to perform
            RUNNING = False
        mouse()
        ListOfEntities = EntityCheckList(ListOfEntities)
        ListOfMBG = MBGCheckList(ListOfMBG, ListOfSBG, ListOfEntities[0])
        pygame.draw.rect(Window, (0, 0, 0), ((0, 0), (1920, 1080)))  # BG
        drawWhole(ListOfDraw, Window)

        clock.tick(MAX_FPS)


if(__name__ == "__main__"):
    startloop()
    main()

pygame.quit()
