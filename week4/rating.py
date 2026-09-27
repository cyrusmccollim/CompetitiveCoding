args = input().split()
judges = int(args[0])
already = int(args[1])

avg = 0
for l in range(already):
    avg += int(input()) / judges

print(avg + (-3 * (judges - already) / judges))
print(avg + (3 * (judges - already) / judges))
