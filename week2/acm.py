# If one box is infected, the neighbor may be too.
# Same boxes are NOT sent consectively.
# How many ways to arrange?
# Output as N % (10^9 + 7)

import sys
sys.setrecursionlimit(10 ** 9)
memory = {}

def recurse(A, C, M, PrevIndex):
    curr = (A, C, M, PrevIndex)
    
    if curr in memory:
        return memory[curr]
    
    numZero = 0

    if A == 0: 
        numZero += 1
    if C == 0: 
        numZero += 1
    if M == 0: 
        numZero += 1
    if numZero >= 2: return 1

    numSelections = 0
    if A > 0 and PrevIndex != 0:
        numSelections += recurse(A - 1, C, M, 0)
    if C > 0 and PrevIndex != 1:
        numSelections += recurse(A, C - 1, M, 1)
    if M > 0 and PrevIndex != 2:
        numSelections += recurse(A, C, M - 1, 2)

    memory[curr] = numSelections
    return numSelections

ACM = [int(n) for n in input().split()]
print(recurse(ACM[0], ACM[1], ACM[2], -1) % (10 ** 9 + 7))