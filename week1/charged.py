import math

def placePotentials():
    for y in range(rows):
        for x in range(cols):
            if ([y + 1, x + 1] in charges):
                continue

            potential = 0
            for q in range(len(charges)):
                rx = abs((x + 1) - (charges[q][1]))
                ry = abs((y + 1) - (charges[q][0]))
                r = math.sqrt(math.pow(rx, 2) + math.pow(ry, 2))
                potential += (chargesSigns[q] * (1 / r)) if r != 0 else 0
            
            if abs(potential) >= (1 / math.pi):
                space[y][x] = "%" if potential < 0 else "0"
            elif abs(potential) >= (1 / math.pow(math.pi, 2)):
                space[y][x] = "X" if potential < 0 else "O"
            elif abs(potential) >= (1 / math.pow(math.pi, 3)):
                space[y][x] = "x" if potential < 0 else "o"
            else:
                space[y][x] = "."


def printSpace():
    str = ""
    for r in range(rows):
        for c in range(cols):
            str += space[r][c]
        str += "\n"
    print(str)

args = input().split(" ")
rows = int(args[0])
cols = int(args[1])
numCharges = int(args[2])

space = [["" for c in range(cols)] for r in range(rows)]
charges = []
chargesSigns = []

for q in range(numCharges):
    chargeInput = input().split(" ")
    x = int(chargeInput[0])
    y = int(chargeInput[1])
    space[x - 1][y - 1] = chargeInput[2]
    sign = 1 if chargeInput[2] == "+" else -1
    charges.append([y, x])
    chargesSigns.append(sign)

placePotentials()
printSpace()