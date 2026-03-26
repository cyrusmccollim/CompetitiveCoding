legals = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, -2], [1, 2], [-1, -2], [-1, 2]]
paths = [] # [[ [0, 0], [2, 1] ], [ ... ], ...]
visited = []
finals = []

def chessToCoords(string):
    res = []
    res.append(ord(string[0]) - 97)
    res.append(int(string[1]) - 1)
    return res

def coordsToChess(coords):
    res = ""
    res += chr(int(coords[0]) + 97)
    res += str(int(coords[1]) + 1)
    return res

def begin(start):
    paths.append([start])
    stop = False

    while len(paths) != 0:
        # print(toVisit)

        currPath = paths.pop(0)
        curr = currPath[-1]

        if curr not in visited: visited.append(curr)

        for delta in legals:
            coords = [0, 0]
            coords[0] = curr[0] + delta[0] 
            coords[1] = curr[1] + delta[1] 

            if (coords[0] < 0 or coords[0] > 7 or coords[1] < 0 or coords[1] > 7):
                continue
            elif (coords in visited):
                continue
            else:
                newPath = currPath + [coords]

                if (coords[0] == target[0] and coords[1] == target[1]):
                    stop = True
                    finals.append(newPath)
                else:
                    paths.append(newPath)
        
        if stop and len(paths) > 0 and len(paths[0]) > len(currPath):
            return

start = chessToCoords(input())
target = chessToCoords(input())

begin(start)

answers = []
for path in finals:
    answer = ""
    for square in path:
        answer += coordsToChess(square) + " -> "
    answers.append(answer[0:-4])

answers.sort()
for a in answers:
    print(a)