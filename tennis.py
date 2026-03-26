def validate(set):
    p = [int(i) for i in set.split(":")]

    larger = 0
    smaller = 1
    if p[1] > p[0]:
        larger = 1
        smaller = 0
    
    if p[larger] == 6 and p[larger] - p[smaller] >= 2:
        return True
    elif p[larger] == 7 and p[larger] - p[smaller] == 1:
        return True
    elif p[larger] == 7 and p[larger] - p[smaller] == 2:
        return True
    else:
        return False
    
def validateThird(set):
    p = [int(i) for i in set.split(":")]

    larger = 0
    smaller = 1
    if p[1] > p[0]:
        larger = 1
        smaller = 0
    
    if p[larger] == 6 and p[larger] - p[smaller] >= 2:
        return True
    elif p[larger] > 6 and p[larger] - p[smaller] == 2:
        return True
    else:
        return False
    
def winner(set):
    p = [int(i) for i in set.split(":")]
    
    larger = 0
    if p[1] > p[0]:
        larger = 1
        
    return larger
    
def loser(set):
    p = [int(i) for i in set.split(":")]
    
    smaller = 1
    if p[1] > p[0]:
        smaller = 0
        
    return smaller

def main():
    names = input().split(" ")
    str = ""
    matches = int(input())
    for m in range(matches):
        res = input().split(" ")
    
        if len(res) >= 2 and len(res) <= 3 and validate(res[0]) and validate(res[1]):
            w1 = winner(res[0])
            w2 = winner(res[1])
            
            if names[loser(res[0])] == "federer" or names[loser(res[1])] == "federer":
                str += "ne\n"
                continue
            
            if (w1 != w2) and len(res) > 2:
                if validateThird(res[2]):
                    if names[loser(res[2])] == "federer":
                        str += "ne\n"     
                    else:
                        str += "da\n"
                else:
                    str += "ne\n"
            elif (w1 == w2) and len(res) <= 2:
                str += "da\n"
            else:
                str += "ne\n"
        else:
            str += "ne\n"            
    return str
    
print(main())
    