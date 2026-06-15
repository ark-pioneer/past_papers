chars1 = list(input())
chars2 = list(input())
valid = True
i = 0

while i < len(chars1):
    char = chars1[i]
    if char in chars2:
        chars2.remove(char)
    else:
        valid = False
        break
    i+=1

if valid:
    print(True)
else:
    print(False)
