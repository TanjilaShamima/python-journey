with open("data.text", "r") as file:
  text = file.read().lower()

text_without_punctuation = ""
for ch in text:
  if ch.isalnum() or ch.isspace():
    text_without_punctuation += ch

words = text_without_punctuation.split()

freq = {}

for word in words:
  if word in freq:
    freq[word] += 1;
  else:
    freq[word] = 1

max_word = ""
max_count = 0

for key in freq:
  if freq[key] > max_count:
    max_count = freq[key]
    max_word = key

print(max_word)
