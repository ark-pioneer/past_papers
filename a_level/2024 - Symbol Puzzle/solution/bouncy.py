while True:
    num = int(input())
    if num > 0 :
        break

digits = str(num)

changes = []
i = 1
while i < len(digits):
    if int(digits[i]) < int(digits[i-1]):
        changes.append("decreasing")
    elif int(digits[i]) == int(digits[i-1]):
        changes.append("same")
    elif int(digits[i]) > int(digits[i-1]):
        changes.append("increasing")
    i += 1

i_count = changes.count("increasing") 
d_count = changes.count("decreasing")
s_count = changes.count("same")

if 0 in [i_count, d_count]:
    print("Not a bouncy number")
elif i_count != 0  and d_count != 0:
    if i_count == d_count:
        print("Perfectly bouncy!")
    else:
        print("Bouncy!")

