import math

def euclidean_distance(A, B):
    """A and B are (x, y) tuples"""
    dx = B[0] - A[0] # B[0] is the x-coordinate of point B, A[0] is the x-coordinate of point A
    dy = B[1] - A[1] # B[1] is the y-coordinate of point B, A[1] is the y-coordinate of point A

    return math.sqrt(dx**2 + dy**2) # Return the Euclidean distance between points A and B

A = (-4, 2)
B = (3, -2)

distance = euclidean_distance(A, B)
print(f"The Euclidean distance between points A{A} and B{B} is: {distance}")

# Using numpy for the same calculation
import numpy as np

A_np = np.array(A)
B_np = np.array(B)
distance_np = np.linalg.norm(B_np - A_np) # np.linalg.norm full form is the norm of a vector, which in this case is the Euclidean distance between two points in n-dimensional space
print(f"The Euclidean distance between points A{A} and B{B} using numpy is: {distance_np}")