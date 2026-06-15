print("Enter an integer greater than 1:")
x = int(input())
product = 1
factor = 0
while product < x:
    factor += 1
    product *= factor
    print(product, factor)
if x == product:
    product = 1
    for n in range(1, factor + 1):
        product *= n
        print(n)
else:
    print("No result")