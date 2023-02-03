import pygame
pygame.init()

Screen = [1920, 1080]

#älä muuta, kaikki kusee sitte
#frames per second

POSSIBLE_ACTIONS = {"Up": moveUp(), "Down": moveDown(), "Left": moveLeft(), "Right": moveRight(), "Jump": jump(), "Quit": ()}

RUNNING = True

#main loop

def main():
    Window = pygame.display.set_mode((Screen[0], Screen[1]))
    PressedKeys = []
    clock = pygame.time.Clock()
    MAX_FPS = 30
    
    while(RUNNING):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        if(pygame.key.get_focused): #only do main loop while window focused
            PressedKeys = getInput() #actions to perform
            actionDoer()
        else:
            pass

        


        clock.tick(MAX_FPS)

if(__name__ == "__main__"):
    main()

pygame.quit()
