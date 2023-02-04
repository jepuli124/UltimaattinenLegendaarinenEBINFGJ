

class ENTITY:
    def __init__(self, VelocityX, VelocityY, characterHeightX, characterHeightY, MovementAcceleration, PosX, PosY, sprite):
        self.VelocityX = VelocityX #pixels / tick
        self.VelocityY = VelocityY #pixels / tick
        self.characterHeightX = characterHeightX #pixels
        self.characterHeightY = characterHeightY #pixels
        self.MovementAcceleration = MovementAcceleration #pixels / tick^2
        self.PosX = PosX
        self.PosY = PosY
        self.sprite = sprite

class PROJECTILE(ENTITY):
    pass

class PLAYER:
    def __init__(self, VelocityX, VelocityY, characterHeightX, characterHeightY, MovementAcceleration, PosX, PosY, sprite):
        self.VelocityX = VelocityX  # pixels / tick
        self.VelocityY = VelocityY  # pixels / tick
        self.characterHeightX = characterHeightX  # pixels
        self.characterHeightY = characterHeightY  # pixels
        self.MovementAcceleration = MovementAcceleration  # pixels / tick^2
        self.PosX = PosX
        self.PosY = PosY
        self.jumpStregth = 4 #velocity given when jumping
        self.sprite = sprite


class NPC(ENTITY):
    pass


class MBG:
    def __init__(self, VelocityX, VelocityY, characterHeightX, characterHeightY, PosX, PosY, sprite):
        self.VelocityX = VelocityX  # pixels / tick
        self.VelocityY = VelocityY  # pixels / tick
        self.characterHeightX = characterHeightX  # pixels
        self.characterHeightY = characterHeightY  # pixels
        self.PosX = PosX
        self.PosY = PosY
        self.sprite = sprite

    def destroy(self):
        if self.PosX <= 0 or self.PosX >= 1920:
            return 1
        elif self.PosY < 0 or self.PosY >= 1080:
            return 1
