def init():
    for r in range(rows):
        frame1.append( list(input()) )
        for c in range(len(frame1[-1])):
            if (frame1[r][c] != x):
                final_frame[r][c] = frame1[r][c]
            else:
                coords1.append([r, c])
    input()
    for r in range(rows):
        frame2.append( list(input()) )
        for c in range(len(frame2[-1])):
            if (frame2[r][c] != x):
                final_frame[r][c] = frame2[r][c]
            else:
                coords2.append([r, c]) 

def get_topleft(coords, coords2):
    if len(coords) < 1 or len(coords2) < 1:
        return 0, 0, 0, 0
    
    minR = coords[0][0]
    minC = coords[0][1]
    minR2 = coords2[0][0]
    minC2 = coords2[0][1]
    for i in range(len(coords)):
        if (coords[i][0] < minR):
            minR = coords[i][0]
        if (coords[i][1] < minC):
            minC = coords[i][1]

        if (coords2[i][0] < minR2):
            minR2 = coords2[i][0]
        if (coords2[i][1] < minC2):
            minC2 = coords2[i][1]
        
    return minR, minC, minR2, minC2

first_line = input()
args = first_line.split()
rows = int(args[0])
cols = int(args[1])
x = args[2][1:-1]

frame1 = []
coords1 = []
start1 = [0, 0]

frame2 = []
coords2 = []
start2 = [0, 0]

final_frame = [[0 for _ in range(cols)] for _ in range(rows)]

init()

start1[0], start1[1], start2[0], start2[1] = get_topleft(coords1, coords2)

displacement = [start2[0] - start1[0], start2[1] - start1[1]] # row and col displacement as [+r, +c]

start3 = [start2[0] + displacement[0], start2[1] + displacement[1]]

for coord in coords1:
    r = start3[0] + (coord[0] - start1[0])
    c = start3[1] + (coord[1] - start1[1])

    if (r < 0 or r > rows-1 or c < 0 or c > cols-1):
        continue

    final_frame[r][c] = x

output_lines = []
for r in range(rows):
    output_lines.append("".join(final_frame[r])) 

print("\n".join(output_lines))