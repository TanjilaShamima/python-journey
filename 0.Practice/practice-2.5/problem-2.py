# Write a Python generator function called batch_generator. It should take a list of numbers (representing data samples) and a batch_size. The generator should yield one batch at a time as a list.

# Example Input:
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# batch_size = 3

# Expected Output (when iterated):
# [1, 2, 3]
# [4, 5, 6]
# [7, 8]

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        print(f"Generating batch from index {i} to {i + batch_size}")  # Debug statement to show the current batch range
        value = data[i:i + batch_size]
        print(f"Current batch: {value}")  # This will print the current batch before yielding it
        yield value

# without using yield
def batch_generator_without_yield(data, batch_size):
    batches = []
    for i in range(0, len(data), batch_size):
        print(f"Generating batch from index {i} to {i + batch_size} without yield")  # Debug statement to show the current batch range
        print(f"Current batch without yield: {data[i:i + batch_size]}")
        batches.append(data[i:i + batch_size])
    return batches

input_data = input()
data = list(map(int, input_data.split(',')))
batch_size = int(input())

for batch in batch_generator(data, batch_size):
    print(batch)

for batch in batch_generator_without_yield(data, batch_size):
    print(batch)

# yield is used to create a generator, which allows us to iterate through the batches one at a time without storing them all in memory at once. This is especially useful when dealing with large datasets.