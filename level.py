import pygame
from classes import TILE

def readLevelFile(LevelFileName, Screen):
    try:
        File = open(LevelFileName, 'r', encoding='UTF-8')
        Lines = File.readlines()
        File.close()
    except:
        pygame.quit()
    Level = []
    x = -1
    y = -1
    for Line in Lines:
        y += 1
        for Char in Line:
            x += 1
            if(Char.isspace() is False):
                Level.append(TILE(Char, x, y, Screen))
            x = -1
    return Level