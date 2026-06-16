print("how many digits? ")
digit_count = int(input())
nums = [input("enter num: ") for i in range(digit_count)]
data = { "frequency": 0 }
for num in nums:
  if num in list(data.keys()):
    data[num] += 1
  else:
    data[num] = 1
    
  if data[num] > data["frequency"]:
    data["number"] = num
    data["frequency"] = data[num]
    data["multimodal"] = False
  elif data[num] == data["frequency"]:
    data["multimodal"] = True
  
if data["multimodal"]:
  print("Data is multimodal")
else:
  print(f"Mode digit is: {data['number']}")
  print(f"Frequency is: {data['frequency']}")


# count = int(input())
# nums = {}
# high = {"0":0}
# multimodal = False

# for _i in range(count):
#     num = int(input())
#     if nums.get(num) == None:
#         nums[num] = 1
#     else:
#         nums[num] += 1

#     current_high_count = list(high.values())[0]
#     if nums[num] > current_high_count:
#         multimodal = False
#         high = {num: nums[num]}
#     elif nums[num] == current_high_count:
#         multimodal = True

# if multimodal:
#     print("Data was multimodal")
# else:
#     print(list(high.values())[0])