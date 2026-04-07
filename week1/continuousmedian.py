cases = int(input())

for case in range(cases):
    input()
    arr = input().split(" ")
    arr = [int(i) for i in arr]

    sum = 0
    for i in range(len(arr)):
        subArrLen = i + 1
        arr2 = arr[:subArrLen]
        arr2.sort()

        odd = subArrLen % 2 != 0
        if (odd): 
            sum += arr2[subArrLen // 2]
        else:
            mid2 = subArrLen // 2
            mid1 = mid2 - 1
            sum += (arr2[mid2] + arr2[mid1]) // 2

    print(sum)
    