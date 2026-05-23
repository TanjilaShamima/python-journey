def compute(a, b):
  try:
    result = ((a**2 + b**2)) / (a-b)
    return result
  except ZeroDivisionError:
    return "Error: Division not possible"


a, b = map(float, input().split())
result = compute(a, b)
print(result)