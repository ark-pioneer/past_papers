digits = input()

while int(digits) < 0:
    digits = input()

i = 1
changes = []
while i < len(digits):
    if digits[i] > digits[i-1]:
        changes.append("increasing")
    elif digits[i] < digits[i-1]:
        changes.append("decreasing")
    i+=1

increasing = changes.count("increasing")
decreasing = changes.count("decreasing")

if increasing > 0 and decreasing > 0:
    if increasing == decreasing:
        result = "perfectly bouncy"
    else:
        result = "bouncy"
else:
    result = "not bouncy"

print(f"{digits} is {result}")