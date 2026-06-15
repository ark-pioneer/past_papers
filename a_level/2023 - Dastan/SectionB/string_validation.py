def unique(data):
  for i in data:
    if data.count(i) > 1:
      return False
  return True

def ascii_sum(data):
  return sum(ord(char) for char in list(data))

def validate(data):
  if len(data) not in range(5, 8):
    return False
  elif data != data.upper():
    return False
  elif not unique(data):
    return False
  elif ascii_sum(data) not in range(420, 601):
    return False
  return True
  
valid = False
while not valid:
  print("enter data: ")
  data = input()
  valid = validate(data)
  print(f"valid: {valid}")
