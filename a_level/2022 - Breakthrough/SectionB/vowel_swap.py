def find_vowel(data, ordinal):
  count = 1
  for char in data:
    if char in 'aeiou':
      if count == ordinal:
        return char
      else:
        count += 1
        
text = input()
text_reverse = "".join([text[i] for i in range(len(text)-1, -1, -1)])
result = ''
vc = 0
for char in text:
  if char in 'aeiou':
    vc += 1
    result += find_vowel(text_reverse, vc)
  else:
    result += char
print(result)