def harshad(n):
    harshad_nums = []
    number = 1
    while len(harshad_nums) < n:
        digits = [int(num) for num in list(str(number))]
        total = sum(digits)
        if number % total == 0:
            harshad_nums.append(number)
        number += 1
    return harshad_nums[-1]

print(harshad(11), 12)
print(harshad(12), 18)



# print("enter n: ")
# nth_h = int(input())
# harshad_nums = []
# num = 1
# while True:
#   if len(harshad_nums) == nth_h:
#     break
#   sum_digits = sum(int(i) for i in str(num))
#   if num % sum_digits == 0:
#     harshad_nums.append(num)
#   num += 1

# print(harshad_nums[-1])