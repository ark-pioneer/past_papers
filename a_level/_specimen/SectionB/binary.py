print("enter num: ")
num = int(input())
bin = []
while num != 0:
  bin.insert(0, str(num % 2))
  num = num // 2

print("".join(bin))