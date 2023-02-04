import pygame
import classes
import random


def createPlayer(ListOfThem, sprite):
    ListOfThem.append(classes.PLAYER(0.0, 0.0, 32, 41, 2, 0.0, 0.0, sprite))
    return ListOfThem


def createEntity(ListOfThem, Vx, Vy, Ch, Cv, Ac, Px, Py, Sprite):
    ListOfThem.append(classes.ENTITY(Vx, Vy, Ch, Cv, Ac, Px, Py, Sprite))
    return ListOfThem


def createMBG(ListOfThem, ListOfSprites):
    b = random.randint(0, 20)
    if b == 1:
        ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, 1900), 0.0, ListOfSprites[0]))
    elif b == 2:
        ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, 1900), 0.0, ListOfSprites[1]))
    elif b == 3:
        ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, 1900), 0.0, ListOfSprites[2]))
    elif b == 4:
        ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, 1900), 0.0, ListOfSprites[3]))
    elif b == 5:
        ListOfThem.append(classes.MBG(random.randint(-10, 10)/10, b/2, 0, 0, random.randint(20, 1900), 0.0, ListOfSprites[4]))
    return ListOfThem


def updatePlayerPos(Player, level): # Currently not used
    TestablePlayerPos = updatePlayerVelocity(Player)
    CollisionDetectionRange = ceil((sqrt(Player.characterHeightX ^ 2 + Player.characterHeightY ^ 2) + Player.maxVelocity) / 32)
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
    elif entity.PosX > 1920-entity.characterHeightX:
        entity.PosX = 1920-entity.characterHeightX
    entity.PosY += entity.VelocityY
    if entity.PosY < 0:
        entity.PosY = 0
    elif entity.PosY > 1080-entity.characterHeightY:
        entity.PosY = 1080-entity.characterHeightY


def MovementReverseX(Entity):
    Entity.VelocityX = (-1) * Entity.VelocityX
    return Entity


def MovementReverseY(Entity):
    Entity.VelocityY = (-1) * Entity.VelocityY
    return Entity


def randomMGBGenerator(ListOfThem, ListOfSprites):
    ListOfThem = (createMBG(ListOfThem,  ListOfSprites))
    return ListOfThem


def EntityCheckList(list):
    for Entity in list:
        # gravity(Entity)
        movement(Entity)
        momentResistanece(Entity)
    return list
    # Player = updatePlayerPos(Player, level)


def MBGCheckList(List, List2, Player):
    List = (randomMGBGenerator(List, List2))
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
    # List = (randomMGBGenerator(List, List2))
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
