# Given a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.
# Sample Input:
#  No input
# Sample Output:
# [4, 16, 36]


number = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, number))
print(even_numbers) # Output: [2, 4, 6]
squared_evens = list(map(lambda x: x**2, even_numbers))
print(squared_evens) # Output: [4, 16, 36]
