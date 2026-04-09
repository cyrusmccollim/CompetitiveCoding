args = input()
digitCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for char in args:
    digitCounts[int(char)] += 1

MIN = 1
for i in range(1, 10):
    if digitCounts[i] < digitCounts[MIN]:
        MIN = i

if digitCounts[0] < digitCounts[MIN]:
    print("1" + ("0" * (digitCounts[0] + 1)))
else:
    print(str(MIN) * (digitCounts[MIN] + 1))
