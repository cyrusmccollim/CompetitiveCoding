def run():
    num_lockers = int(input())
    lockers = input().split()
    sums = {}

    for i in range(len(lockers)):
        sums[int(lockers[i])] = 1

        for j in range(len(lockers)):
            if (i == j): 
                continue
            res = int(lockers[i]) + int(lockers[j])
            if (res in sums):
                return res
            else:
                sums[res] = 1

print(run())