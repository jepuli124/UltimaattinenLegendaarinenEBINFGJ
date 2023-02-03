import pygame

def actionDoer(Actions, Player):
    for Action in Actions:
        if(Action == "Up"):
            Player = moveUp(Player)
        elif(Action == "Down"):
            Player = moveDown(Player)
        elif(Action == "Left"):
            Player = moveLeft(Player)
        elif(Action == "Right"):
            Player = moveRight(Player)
        elif(Action == "Jump"):
            Player = jump(Player)
        elif(Action == "quit"):
            pygame.quit()
    return Player

            
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

def moveRight():
    global Player
    Player.VelocityX += Player.playerMovementAcceleration
    return

def jump():
    global Player
    Player.VelocityY = Player.jumpStrength
    return

def detectEntityCollision(entity1, entity2):
    #entity1 on pelaajahahmo, jos se on osa tarkastusta
    #katsotaan onko entity:t päällekkäin x-suunnassa
    if((entity1.playerPosX <= entity2.playerPosX + entity2.playerPosX) or (entity1.playerPosX + entity1.characterHeightX >= entity2.characterHeightX)):
        #katsotaan onko entity:t päällekkäin y-suunnassa
        if((entity1.playerPosY <= entity2.playerPosY + entity2.playerPosY) or (entity1.playerPosY + entity1.characterHeightY >= entity2.characterHeightY)):
            if(entity1.VelocityY > 0):
                return True, True
            return True, False
    return False, False


