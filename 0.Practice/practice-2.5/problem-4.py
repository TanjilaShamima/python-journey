# Write a function power(base, exponent) that returns the result of base raised to exponent. If the exponent is not given, it should calculate the square.
# Sample Input:
# 5
# Sample Output:
# 25
# Sample Input 2:
# 5 3
# Sample Output 2:
# 125


def power(base, exponent=2):
    return base ** exponent


input_data = input().split()
base = int(input_data[0])
if len(input_data) > 1:
    exponent = int(input_data[1])
else:
    exponent = 2

print(power(base, exponent))