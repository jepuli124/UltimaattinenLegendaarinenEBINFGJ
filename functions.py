import main
import pygame
import classes
import random
from classes import *
from main import *
from math import sqrt, ceil, floor

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


def createPlayer(ListOfThem, sprite):
    ListOfThem.append(classes.PLAYER(0.0, 0.0, 32, 41, 2, 0.0, 0.0, sprite))
    return ListOfThem


def createEntity(ListOfThem, Vx, Vy, Ch, Cv, Ac, Px, Py, Sprite):
    ListOfThem.append(classes.ENTITY(Vx, Vy, Ch, Cv, Ac, Px, Py, Sprite))
    return ListOfThem


def createMBG(ListOfThem, ListOfSprites, a):
    b = random.randint(0, 20)
    if a:
        if b == 1:
            ListOfThem.append(
                classes.MBG(random.randint(-10, 10) / 10, b / 2, 0, 0, 0.0, random.randint(2, main.Screen[1]-5), ListOfSprites[0]))
        elif b == 2:
            ListOfThem.append(
                classes.MBG(random.randint(-10, 10) / 10, b / 2, 0, 0, 0.0, random.randint(2, main.Screen[1]-5), ListOfSprites[1]))
        elif b == 3:
            ListOfThem.append(
                classes.MBG(random.randint(-10, 10) / 10, b / 2, 0, 0, 0.0, random.randint(2, main.Screen[1]-5), ListOfSprites[2]))
        elif b == 4:
            ListOfThem.append(
                classes.MBG(random.randint(-10, 10) / 10, b / 2, 0, 0, 0.0, random.randint(2, main.Screen[1]-5), ListOfSprites[3]))
        elif b == 5:
            ListOfThem.append(
                classes.MBG(random.randint(-10, 10) / 10, b / 2, 0, 0, 0.0, random.randint(2, main.Screen[1]-5), ListOfSprites[4]))
    else:
        if b == 1:
            ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(10, main.Screen[0]-5), 0.0, ListOfSprites[0]))
        elif b == 2:
            ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, main.Screen[1]-5), 0.0, ListOfSprites[1]))
        elif b == 3:
            ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, main.Screen[1]-5), 0.0, ListOfSprites[2]))
        elif b == 4:
            ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, main.Screen[1]-5), 0.0, ListOfSprites[3]))
        elif b == 5:
            ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, main.Screen[1]-5), 0.0, ListOfSprites[4]))
    return ListOfThem


def updatePlayerPos(Player, level): # Currently not used
    TestablePos = updatePlayerVelocity(Player)
    CollisionDetectionRange = ceil((sqrt(Player.characterHeightX ^ 2 + Player.characterHeightY ^ 2) + Player.maxVelocity) / 32)
    i = 0
    j = 0
    for Line in level:
        for Tile in Line:
            OldPos = [Player.PosY, Player.PosX]
            NewPos = TestablePos.copy()
            FinalPlayerPos = TestablePos.copy()
            while(CharacterInsideTile(FinalPlayerPos, Player, level, i ,j)):
                TestPos = [round(average([NewPos[0], OldPos[0]])), round(average([NewPos[1], OldPos[1]]))]
                if(CharacterInsideTile(TestPos, Player, level, i ,j)):
                    OldPos = TestPos.copy()
                elif(getDistance < 2):
                    FinalPos = TestPos.copy
                else:
                    NewPos = TestPos.copy()
            j += 1
        i += 1
    Player.PosX = FinalPos[0]
    Player.PosY = FinalPos[1]
    return Player

def average(ListOfNumbers):
    Sum = 0
    for Number in ListOfNumbers:
        Sum += Number
    return Sum / len(ListOfNumbers)

def getDistance(Pos1, Pos2):
    if(Pos1[0]-Pos2[0] < 0):
        y = (-1) * Pos1[0]-Pos2[0]
    else:
        y = Pos1[0]-Pos2[0]
    if(Pos1[1]-Pos2[2] < 0):
        x = (-1) * Pos1[1]-Pos2[1]
    else:
        x = Pos1[1]-Pos2[1]
    return sqrt(y^2 + x^2)


def CharacterInsideTile(TestablePlayerPos, Player, y, x):
    if (TestablePlayerPos[0] <= y + 32) and (TestablePlayerPos[0] + Player.characterHeightX >= y):
        if (TestablePlayerPos[1] <= x + 32) and (TestablePlayerPos[1] + Player.characterHeightY >= x):
            return True
    return False


def updatePlayerVelocity(Player):
    return [Player.playerPosY + Player.VelocityY, Player.playerPosX + Player.VelocityX]


def getInput(Player):
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        return 1
    if key[pygame.K_UP]:
        moveY(Player, 1)
    if key[pygame.K_DOWN]:
        moveY(Player, -1)
    if key[pygame.K_LEFT]:
        moveX(Player, -1)
    if key[pygame.K_RIGHT]:
        moveX(Player, 1)
    if key[pygame.K_SPACE]:
        moveY(Player, 1)


def mouse():
    c1 = pygame.mouse.get_pressed(num_buttons=3)
    e1 = pygame.mouse.get_pos()
    if c1:
        return [True, e1]
    else:
        return [False, e1]


def moveY(Entity, Times):
    Entity.VelocityY += Entity.MovementAcceleration * Times * (-1)
    return Entity


def moveX(Entity, Times):
    Entity.VelocityX += Entity.MovementAcceleration * Times
    return Entity


def jump(Entity):
    Entity.VelocityY = Entity.jumpStrength
    return Entity


def gravity(Entity): #TODO Grounded
    if (Entity.grounded is False):
        Entity.VelocityY += 1
    return Entity


def momentResistanece(Entity):
    Entity.VelocityY = Entity.VelocityY * 0.9
    Entity.VelocityX = Entity.VelocityX * 0.9


def movement(entity):
    entity.PosX += entity.VelocityX
    if entity.PosX < 0:
        entity.PosX = 0
    elif entity.PosX > Screen[0]-entity.characterHeightX:
        entity.PosX = Screen[0]-entity.characterHeightX
    entity.PosY += entity.VelocityY
    if entity.PosY < 0:
        entity.PosY = 0
    elif entity.PosY > Screen[1]-entity.characterHeightY:
        entity.PosY = Screen[1]-entity.characterHeightY


def MovementReverseX(Entity):
    Entity.VelocityX = (-1) * Entity.VelocityX
    return Entity


def MovementReverseY(Entity):
    Entity.VelocityY = (-1) * Entity.VelocityY
    return Entity


def randomMGBGenerator(ListOfThem, ListOfSprites, a):
    ListOfThem = (createMBG(ListOfThem,  ListOfSprites, a))
    return ListOfThem


def EntityCheckList(list):
    for Entity in list:
        # gravity(Entity)
        movement(Entity)
        momentResistanece(Entity)
    return list
    # Player = updatePlayerPos(Player, level)


def MBGCheckList(List, List2, Player):
    List = (randomMGBGenerator(List, List2, 0))
    counter = 0
    for Entity in List:
        movement(Entity)
        Dest = Entity.destroy()
        if Dest == 1:
            List.pop(counter)
        if detectEntityCollision(Player, Entity):
            List.pop(counter)
        counter += 1

    return List


def MBGCheckListWP(List, List2):
    List = (randomMGBGenerator(List, List2, 1))
    counter = 0
    for Entity in List:
        movement(Entity)
        Dest = Entity.destroy()
        if Dest == 1:
            List.pop(counter)
        counter += 1

    return List


def detectEntityCollision(entity1, entity2):
    # entity1 on pelaajahahmo, jos se on osa tarkastusta
    # katsotaan onko entity:t päällekkäin x-suunnassa
    if (entity1.PosX <= entity2.PosX + entity2.characterHeightX) and (entity1.PosX + entity1.characterHeightX >= entity2.PosX):
        # katsotaan onko entity:t päällekkäin y-suunnassa
        if (entity1.PosY <= entity2.PosY + entity2.characterHeightY) and (entity1.PosY + entity1.characterHeightY >= entity2.PosY):
            return True
    return False


def drawWhole(ListOfList, display):
    for List in ListOfList:
        for Object in List:
            display.blit(Object.sprite, (Object.PosX, Object.PosY))  # Piirtää listanmukaisesti jokaisen objectin
    pygame.display.flip()

