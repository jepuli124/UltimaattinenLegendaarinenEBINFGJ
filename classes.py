class ENTITY():
    def __init__(self, VelocityX, VelocityY, characterHeightX, characterHeightY, playerMovementAcceleration, playerPosX, playerPosY):
        self.VelocityX = VelocityX #pixels / tick
        self.VelocityY = VelocityY #pixels / tick
        self.characterHeightX = characterHeightX #pixels
        self.characterHeightY = characterHeightY #pixels
        self.playerMovementAcceleration = playerMovementAcceleration #pixels / tick^2
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.jumpStregth = 4 #velocity given when jumpig
        self.maxVelocity = 4 #pixels / tick



