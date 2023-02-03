import pygame
pygame.init()

Screen = [1920, 1080]



#älä muuta, kaikki kusee sitte
MAX_FPS = 30 #frames per second
CHARACTER_HEIGTH = 60 #pixels

possibleActions = {"Up": moveUp(), "Down": moveDown(), "Left": moveLeft(), "Right": moveRight(), "Jump": jump(), "Quit": ()}

running = True

#main loop

def main():
    pressedKeys = []
    PlayerVelocityX = 0.0
    PlayerVelocityY = 0.0
    while(running):


        if(pygame.key.get_focused): #only do main loop while window focused
            pressedKeys = getInput() #actions to perform
            for action in pressedKeys:
            pass    
                
            
        else:
            pass

if(__name__ == "__main__"):
    main()
