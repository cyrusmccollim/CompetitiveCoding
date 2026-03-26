import sys

def simQuests(pool, energy):
    if not pool: return 0
    gold = 0
    i = len(pool) - 1
    while i >= 0 and energy >= pool[0][0]:
        if pool[i][0] <= energy:
            energy -= pool[i][0]
            gold += pool[i][1]
            pool.pop(i)
        i -= 1
    return gold

lines = sys.stdin.read().split("\n")
lines = lines[1:]

quests = []
sort = False

for line in lines:
    cmd = line.split()
    if len(cmd) < 1: 
        continue
    if cmd[0] == "add":
        quests.append([int(cmd[1]), int(cmd[2])])
        sort = True
    elif cmd[0] == "query":
        if sort:
            quests.sort()
            sort = False
        print(simQuests(quests, int(cmd[1])))