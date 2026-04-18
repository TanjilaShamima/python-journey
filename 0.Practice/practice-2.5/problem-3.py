#  Given a list [1,2,3,4], use map() and lambda to create a new list with squares of each number.

# Sample Input:
#  No input

# Sample Output:
# [1, 4, 9, 16]

def square_numbers(numbers):
    squared_numbers = list(map(lambda x: x**2, numbers))
    return squared_numbers

# List of integers after mapping
input_numbers = list(map(int, input().split(',')))
result = square_numbers(input_numbers)
print(result)
    
