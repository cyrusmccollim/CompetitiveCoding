import math

cards = list(input())
counts = [0, 0, 0]
for c in cards:
    if c == "T":    counts[0] += 1
    elif c == "C":  counts[1] += 1
    elif c == "G":  counts[2] += 1

bonus = 0
m = min(counts)
if (counts[0] - m >= 0 and counts[1] - m >= 0 and counts[2] - m >= 0):
    bonus += m * 7

print( int(
        math.pow(counts[0], 2) +
        math.pow(counts[1], 2) +
        math.pow(counts[2], 2) +
        bonus
       )
     )
