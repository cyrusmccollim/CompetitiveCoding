numCars = int(input())
weights = []
frontMaxAdds = []
backMaxAdds = []

for i in range(numCars):
    val = int(input())
    weights.append(val)
    frontMaxAdds.append(1)
    backMaxAdds.append(1)

weights.reverse()

for i in range(numCars):
    for j in range(i):
        if weights[j] < weights[i]:
            if frontMaxAdds[j] + 1 > frontMaxAdds[i]:
                frontMaxAdds[i] = frontMaxAdds[j] + 1
        if weights[j] > weights[i]:
            if backMaxAdds[j] + 1 > backMaxAdds[i]:
                backMaxAdds[i] = backMaxAdds[j] + 1

highest = 0
for i in range(numCars):
    total = frontMaxAdds[i] + backMaxAdds[i] - 1
    if total > highest:
        highest = total

print(highest)
