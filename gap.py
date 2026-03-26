mothers = (31 + 28 + 31 + 30 + 14) 
fathers = (31 + 28 + 31 + 30 + 31 + 18) 
day = 6

year = int(input())

def leap(year):
    return (year % 4 == 0) and (not year % 100 == 0 or year % 400 == 0)

for i in range(2000, year):
    if leap(i):
        day = (day + 366) % 7
    else:
        day = (day + 365) % 7

may1 = (day + 120 + (1 if leap(year) else 0)) % 7

if may1 == 0 or may1 >= 5:
    print("6 weeks")
else:
    print("5 weeks")