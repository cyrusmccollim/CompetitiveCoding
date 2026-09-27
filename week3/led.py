args = input().split()
num_src = int(args[0])
cost_per_gate = int(args[1])
constant_cost = int(args[2])
timings = [int(i) for i in input().split()]

while len(timings) > 1:
    timings.sort()
    a = timings.pop(0)
    b = timings.pop(0)
    gate_output = max(a, b) + cost_per_gate
    timings.append(gate_output)

total_time = timings[0] + constant_cost
print(total_time)