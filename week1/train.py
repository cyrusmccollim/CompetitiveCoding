
trainLeft = None
trainRight = None
sum = 0
numCars = int(input())

for car in range(numCars):
    weight = int(input())
    sum += 1
    if (trainLeft == None or trainRight == None):
        trainLeft = weight
        trainRight = weight
    elif (weight > trainLeft):
        trainLeft = weight
    elif (weight < trainRight):
        trainRight = weight
    else:
        sum -= 1

print(sum)







