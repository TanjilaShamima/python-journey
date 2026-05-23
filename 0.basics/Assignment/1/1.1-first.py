given_list = list(map(int, input().split()))

result = []

for num in given_list:
  if num % 3 == 0 and num % 5 != 0:
    result.append(num)

print(result)