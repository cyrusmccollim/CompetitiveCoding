# input 78432579 -> output 20

import itertools

numbers = [int(i) for i in list(input())]

min_time = 999999999
for p in itertools.permutations(range(0, 10)):
    i = 0
    final_time = 0
    while i < len(numbers)-1:
        time = abs(p.index(numbers[i]) - p.index(numbers[i+1]))
        if time == 0: 
            time = 1
        final_time += time
        i += 1

    if final_time < min_time:
        min_time = final_time

print(min_time)