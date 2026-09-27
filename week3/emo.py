def calc(text):
    emoticons = (":-)", ":-(", ";-)", "^_^", "-_-", "^o^", "^^;", "(..)", ":)", "xD")
    length = 0
    i = 0
    n = len(text)
    while i < n:
        for emo in emoticons:
            if text.startswith(emo, i):
                length += 1
                i += len(emo)
                break
        else:
            length += 1
            i += 1    
    return length

s = input()
alpha = [chr(i) for i in range(32, 127)]
lengths = []

for replace in set(s):
    for replacement in alpha:
        new = s.replace(replace, replacement)
        l = calc(new)
        lengths.append(l)

print(min(lengths), end=" ")
print(max(lengths), end=" ")