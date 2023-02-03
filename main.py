import pygame
pygame.init()

Screen = [1920, 1080]
Window = pygame.display.set_mode((Screen[0], Screen[1]))

#älä muuta, kaikki kusee sitte
 #frames per second
CHARACTER_HEIGTH = 60 #pixels

possibleActions = {"Up": moveUp(), "Down": moveDown(), "Left": moveLeft(), "Right": moveRight(), "Jump": jump(), "Quit": ()}

running = True

#main loop

def main():
    clock = pygame.time.Clock()
    MAX_FPS = 30

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if(pygame.key.get_focused): #only do main loop while window focused
            pressedKeys = getInput() #actions to perform
            for action in pressedKeys:
                pass    
                
            
        else:
            pass
        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
