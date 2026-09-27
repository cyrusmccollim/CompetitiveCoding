import itertools

args = input().split()
num_stu = int(args[0])
num_ques = int(args[1])
exams = [list(input().strip()) for i in range(num_stu)]
best = 0

for possiblilty in itertools.product(["T", "F"], repeat=num_ques):
    min_grade = 999
    
    for e in range(num_stu):
        grade = 0
        for q in range(num_ques): 
            if exams[e][q] == possiblilty[q]:
               grade += 1
        if grade < min_grade:
            min_grade = grade
            
    if min_grade > best:
        best = min_grade

print(best)