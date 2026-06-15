print("enter text: ")
data = input()
count = 1
data_c = []
i = 0
while i < len(data):
  if i == len(data) - 1:
    data_c.append(f"{data[i]} {count}")
  elif data[i] != data[i+1]:
    data_c.append(f"{data[i]} {count}")
    count = 1
  else:
    count += 1
  i += 1

print(" ".join(data_c))