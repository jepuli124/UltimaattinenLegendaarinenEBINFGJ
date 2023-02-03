import pygame
pygame.init()

Screen = [1920, 1080]
Window = pygame.display.set_mode((Screen[0], Screen[1]))

#älä muuta, kaikki kusee sitte
 #frames per second
CHARACTER_HEIGTH = 60 #pixels

PlayerVelocityX = 0.0
PlayerVelocityY = 0.0
PlayerPosX = 0.0
playerPosY = 0.0

PossibleActions = {"Up": moveUp(), "Down": moveDown(), "Left": moveLeft(), "Right": moveRight(), "Jump": jump(), "Quit": ()}

Running = True

#main loop

def main():

    PressedKeys = []
    clock = pygame.time.Clock()
    MAX_FPS = 30
    
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if(pygame.key.get_focused): #only do main loop while window focused
            PressedKeys = getInput() #actions to perform
            actionDoer()
        else:
            pass

        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
