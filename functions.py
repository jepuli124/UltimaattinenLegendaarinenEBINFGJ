<<<<<<< HEAD
def actionDoer(Actions):
    global PossibleActions
    for Action in Actions:
        if Action in PossibleActions:
            PossibleActions[Action]
    return
=======
import pygame

def keys():
    Movement = []
    nappain = pygame.key.get_pressed()
    if nappain[pygame.K_ESCAPE]:
        return "exit"
    if nappain[pygame.K_UP]:
        Movement.append("Up")
    if nappain[pygame.K_DOWN]:
        Movement.append("Down")
    if nappain[pygame.K_LEFT]:
        Movement.append("Left")
    if nappain[pygame.K_RIGHT]:
        Movement.append("Right")
    if nappain[pygame.K_SPACE]:
        Movement.append("Space")
    return Movement

def mouse():
    c1 = pygame.mouse.get_pressed(num_buttons=3)
    e1 = pygame.mouse.get_pos()
>>>>>>> 6bd2138faab39623e99ba4537eb51cf24b32e715
