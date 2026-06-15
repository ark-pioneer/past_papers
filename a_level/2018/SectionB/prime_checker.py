def is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
      
while True:
  print("enter num:")
  num = int(input())
  
  if num <= 1:
    print("not greater than 1")
  elif is_prime(num):
    print("is prime")
  else:
    print("is not prime")
      
  print("enter another number? y/n")
  choice = input().lower()
  if choice == 'n':
    break