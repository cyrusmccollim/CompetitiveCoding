# report = 250
# limit = report / 2 = 125
# cost = 150
# reimburse = min(cost, limit) = min(150, 125)
# pay = cost - reimburse = 150 - 125 = 25

num_tickets = int(input())
tickets = []
for i in range(num_tickets):
    tickets.append(int(input()))

tickets.sort()
smallest = tickets[0] 
largest = tickets[num_tickets - 1]
print(int(max(0, smallest - (largest / 2))))


