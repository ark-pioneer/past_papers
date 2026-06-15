# Write a program that uses a transposition cipher to encrypt a string entered by the 
# user.
# After the user enters the string to encrypt, they enter the number of columns to use. 
# Different numbers of columns result in different encrypted versions of the same string.
# Any non-alphabetic characters in the string entered by the user are ignored and will 
# not appear in the encrypted text.
# To encrypt the string, the characters from the user’s input are written into a grid (left to 
# right, top to bottom) of cells which has the number of columns specified by the user. 
# The characters are then read from the grid in a different order (top to bottom,
# left to right).
# Example 1
# If the user enters the string hypothetically and 3 for the number of columns,
# then the encrypted version of that string will be hoeclyttayphil

string = input()
num_cols = int(input())
string2 = "".join([char for char in string if char.isalpha()])
result = ""
for col in range(num_cols):
    i = 0
    while i < len(string2):
        if i % num_cols == col:
            result += string2[i]
        i += 1
print(result)
