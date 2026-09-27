args = input().split()
num_stops = int(args[0])
current_level = int(args[1])

stops = []
destinations = []
for i in range(stops):
    line = split(input())
    stops.append(int(line[0]))
    destinations.append(int(line[1]))

stops.sort()

constant_cost = int(args[2])
timings = [int(i) for i in input().split()]