text = input()
words = text.split()
result = []
for word in words:
  result.append(len(word))

print(result)