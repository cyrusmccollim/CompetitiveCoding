map = {
    "clank": "a",
    "bong": "b",
    "click": "c",
    "tap": "d",
    "poing": "e",
    "clonk": "f",
    "clack": "g",
    "ping": "h",
    "tip": "i",
    "cloing": "j",
    "tic": "k",
    "cling": "l",
    "bing": "m",
    "pong": "n",
    "clang": "o",
    "pang": "p",
    "clong": "q",
    "tac": "r",
    "boing": "s",
    "boink": "t",
    "cloink": "u",
    "rattle": "v",
    "clock": "w",
    "toc": "x",
    "clink": "y",
    "tuc": "z",
    
    "whack": " ",
    "bump": "caps",
    "pop": "del",
    "dink": "shift",
    "thumb": "unshift"
    }
    
num = int(input())
str = ""
caps = False
for i in range(0, num):
    next = map.get(input())
    if next == "caps" or next == "shift" or next == "unshift":
        caps = not caps
    elif next == "del":
        str = str[0:-1]
    elif next == " ":
        str += " "
    else:
        str += chr(ord(next) - (97 -  65)) if caps else next

print(str)
    
    