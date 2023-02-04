def readLevelFromFile(fileToRead):
    try:
        file = open(fileToRead, 'r', encoding="UTF-8")
        lines = file.readlines()
    except:
        print("Error while handling file '{}'".format(fileToRead))
        pygame.quit()
        return "exit"
    level = []
    i = -1
    for line in lines:
        i += 1
        level.append([])
        for character in line:
            if (character != '\n'):
                level[i].append(character)

    longestLine = len(line[0])
    for line in level:
        if (len(line) > longestLine):
            longestLine = line
    for line in level:
        for i in range(longestLine - len(line)):
            line.append(' ')
    file.close()
    return level