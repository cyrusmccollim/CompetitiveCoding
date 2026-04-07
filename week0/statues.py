def f(case):
    count = 0
    heightsCpy = heights[:]

    for k in range(rows + cols - 1):
        r = max(0, k - cols + 1)
        c = min(k, cols - 1)
        
        realR = r
        realC = c
        if case == 2:
            realC = cols - 1 - c
        elif case == 3:
            # W and S
            realR = rows - 1 - r
        elif case == 4:
            # S and E
            realR = rows - 1 - r
            realC = cols - 1 - c

        cellsOnDiagonal = min(k + 1, rows, cols, rows + cols - 1 - k)
        print(heightsCpy)

        heightsOnDiag = [
            heightsCpy.pop(0) 
            for i in range(cellsOnDiagonal) 
            if park[r + i][c - i] != -1
        ]

        while r < rows and c >= 0:

            if park[realR][realC] not in heightsOnDiag:
                count += 1

            r += 1
            c -= 1    

    return count

parkDim = input().split()
rows = int(parkDim[0])
cols = int(parkDim[1])

park = []
heights = []

for i in range(0, rows):
    row = list(map(int, input().split()))
    park.append(row)
    for height in row:
        if height != -1:
            heights.append(height)

heights.sort()

print(min(f(1), f(2), f(3), f(4)))
