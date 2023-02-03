import pygame

def actionDoer(Actions):
    global POSSIBLE_ACTIONS
    for Action in Actions:
        if Action in POSSIBLE_ACTIONS:
            POSSIBLE_ACTIONS[Action]
    return

def getInput():
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

<<<<<<< Updated upstream
def moveUp():
    global Player
    Player.VelocityY -= Player.playerMovementAcceleration
    return

def moveDown():
    global Player
    Player.VelocityY += Player.playerMovementAcceleration
    return

def moveLeft():
    global Player
    Player.VelocityY -= Player.playerMovementAcceleration
    return
    PlayerAcceleration = 1

def moveRight():
    global Player
    Player.VelocityX += Player.playerMovementAcceleration
    return

def jump():
    global Player
    Player.VelocityY = Player.jumpStrength
    return

=======
>>>>>>> Stashed changes
