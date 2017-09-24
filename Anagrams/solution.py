#Radomir Fugiel

import sys

# --- FUNCTIONS ---

def doesItFit(text, fontSize, maxHeight, maxWidth):
    line = ''
    lineCount = 1

    for letter in text:
        if getTotalWidth(line + letter, fontSize) <= maxWidth:
            line += letter
        else:
            lineCount += 1
            line = ''
            line += letter

    if lineCount*fontSize > maxHeight:
        return False
    else:
        return True


def getTotalWidth(text, fontSize):
    total = 0
    for letter in text:
        multiplier = weights[letter]
        total += int(multiplier*fontSize)
    return total

def getMaxSize(maxHeight, maxWidth, text):
    fontSize = 1

    if doesItFit(text, fontSize, maxHeight, maxWidth) == False:
        return 0
    
    while doesItFit(text, fontSize, maxHeight, maxWidth) == True:
        fontSize += 1

    return (fontSize - 1)


# --- MAIN ---

weights = {}
    
for line in sys.stdin:
    curr = line.strip().split(" ")

    #Fill in dict of letter weights
    if (curr[0].isalpha()):
        weights[curr[0]] = float(curr[1])

    else:
        maxHeight = int(curr[0])
        maxWidth = int(curr[1])
        text = curr[2]

        print getMaxSize(maxHeight, maxWidth, text)


