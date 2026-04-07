list = [x for x in range(500)]
target = 10

# print(list) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 499]

def dataGenerator(params, target):
    print("Generator is called", len(params), target)
    for i in range(0, len(params), target):
        yield params[i : i + target]

x = dataGenerator(list, 10)
print(next(x)) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(next(x)) # Output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(next(x)) # Output: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]