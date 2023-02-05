import pygame
from functions import *
from classes import * 
from math import sqrt, ceil, floor
import cv2
import numpy as np

pygame.init()

# load Pictures:

Screen = (480, 256)

leaf1 = pygame.image.load("./textures/leaf1.png")
leaf2 = pygame.image.load("./textures/leaf2.png")
leaf3 = pygame.image.load("./textures/leaf3.png")
leaf4 = pygame.image.load("./textures/leaf4.png")
leaf5 = pygame.image.load("./textures/leaf5.png")
Axe = pygame.image.load("./textures/Axe.png")
cha = pygame.image.load("./textures/päähahmo.png") 
GameBackground = pygame.transform.scale(pygame.image.load("./textures/Forest2.png"), Screen)

bigStartB = pygame.image.load("./textures/tausta.png")
startB = pygame.transform.scale(bigStartB, Screen)
perhonen1 = pygame.transform.scale(pygame.image.load("./textures/perhonen1.png"), (32, 32))
perhonen2 = pygame.transform.scale(pygame.image.load("./textures/perhonen2.png"), (32, 32))
perhonen3 = pygame.transform.scale(pygame.image.load("./textures/perhonen3.png"), (32, 32))
head = pygame.transform.scale(pygame.image.load("./textures/GAME JAM head.png"), (32, 32))
head2 = pygame.transform.scale(pygame.image.load("./textures/GAME JAM head anime.png"), (32, 32))




Window = pygame.display.set_mode((Screen[0], Screen[1]))
pygame.display.set_caption("MOST ULTIMATE LEGEDARY GAME THING EVER")
font = pygame.font.Font('freesansbold.ttf', 75)
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
        #    level = readLevelFromFile(CurrentStage, Screen)
        #    if level == "exit":
        #        RUNNING = False
        #        break
        #    NewStage = False
        if getInput(ListOfEntities[0]) == 1: #actions to perform
            RUNNING = False
        mouse()
        ListOfEntities = EntityCheckList(ListOfEntities)
        ListOfMBG = MBGCheckList(ListOfMBG, ListOfSBG, ListOfEntities[0])
        Window.blit(GameBackground, (0, 0)) # BG
        drawWhole(ListOfDraw, Window)

        clock.tick(MAX_FPS)


def video():
    cap = cv2.VideoCapture('./textures/EBIGLEGENDFJG.mp4')

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

if(__name__ == "__main__"):
    startloop()
    video()
    main()

pygame.quit()
