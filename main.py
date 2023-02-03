import pygame

#älä muuta, kaikki kusee sitte
MAX_FPS = 30 #frames per second
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
    
    while(Running):


        if(pygame.key.get_focused): #only do main loop while window focused
            PressedKeys = getInput() #actions to perform
            actionDoer()
        else:
            pass

if(__name__ == "__main__"):
    main()
