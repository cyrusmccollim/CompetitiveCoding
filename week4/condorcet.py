args = input().split()
num_cand = int(args[0])
num_votes = int(args[1])

candidates = []
matchups = [[0] * num_cand] * num_cand
indexes = {}

first_vote = list(input().split()[0])
i = 0
for c in first_vote:
    indexes[c] = i
    i += 1
    matchups 

for c in range(num_votes):
    vote = input().split()[0]
