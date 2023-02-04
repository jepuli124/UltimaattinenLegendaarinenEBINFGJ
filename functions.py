import pygame

def readLevelFromFile(fileToRead):
    try:
        file = open(fileToRead, 'r', encoding="UTF-8")
        lines = file.readlines()
        file.close()
    except:
        print("Erro while handling file '{}'".format(fileToRead))
        pygame.quit()
    level = []
    i = -1
    for line in lines:
        i += 1
        level.append([])
        for character in line:
            if(character != '\n'):
                level[i].append(character)
    
    longestLine = len(line[0])
    for line in level:
        if(len(line) > longestLine):
            longestLine = line
    for line in level:
        for i in range(longestLine - len(line)):
            line.append(' ')
    return level

def updatePlayerPos(Player, level, CollisionDetectionRange):
    TestablePlayerPos = updatePlayerVelocity(Player)
    i = 0
    j = 0
    for Line in level:
        for Tile in Line:
            if(CharacterInsideTile(TestablePlayerPos, Player, level, i ,j)):
                Player = movePlayerToClearTile(TestablePlayerPos, Player, level)
            j += 1
        i += 1
    return Player

def CharacterInsideTile(TestablePlayerPos, Player, y, x):
    if((TestablePlayerPos[0] <= y + 32) and (TestablePlayerPos[0] + Player.characterHeightX >= y)):
        if((TestablePlayerPos[1] <= x + 32) and (TestablePlayerPos[1] + Player.characterHeightY >= x)):
            return True
    return False

def updatePlayerVelocity(Player):
    return [Player.playerPosY + Player.VelocityY, Player.playerPosX + Player.VelocityX]

def actionDoer(Actions, Player):
    PossibleActions = {"Up": moveUp(Player), "Down": moveDown(Player), "Left": moveLeft(Player), "Right": moveRight(Player), "Jump": jump(Player)}
    for Action in Actions:
        if(Action in PossibleActions):
            if(Action == "exit"):
                pygame.quit()
            Player = PossibleActions[Action]
    return Player

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

def moveUp(Player):
    Player.VelocityY -= Player.playerMovementAcceleration
    return Player

def moveDown(Player):
    Player.VelocityY += Player.playerMovementAcceleration
    return Player

def moveLeft(Player):
    Player.VelocityY -= Player.playerMovementAcceleration
    return Player

def moveRight(Player):
    Player.VelocityX += Player.playerMovementAcceleration
    return Player

def jump(Player):
    Player.VelocityY = Player.jumpStrength
    return Player

def detectEntityCollision(entity1, entity2):
    #entity1 on pelaajahahmo, jos se on osa tarkastusta
    #katsotaan onko entity:t päällekkäin x-suunnassa
    if((entity1.playerPosX <= entity2.playerPosX + entity2.characterHeightX) and (entity1.playerPosX + entity1.characterHeightX >= entity2.playerPosX)):
        #katsotaan onko entity:t päällekkäin y-suunnassa
        if((entity1.playerPosY <= entity2.playerPosY + entity2.characterHeightY) and (entity1.playerPosY + entity1.characterHeightY >= entity2.playerPosY)):
            if(entity1.VelocityY > 0):
                return True, True
            return True, False
    return False, False
