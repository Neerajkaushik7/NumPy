"""
Program Name : 3D Array Using Tuple
Author       : Neeraj Kaushik

Description:
Create a 3D NumPy array using nested tuples and display its
elements using different looping methods.

Example:
Input : 3D array values
Output:
[[[1 2 3]
  [4 5 6]]
 [[1 2 3]
  [4 5 6]]]
"""

import numpy as np

# Implementation:

# Create a 3D NumPy array using nested tuples
multiD = np.array(
    (
        (
            (1, 2, 3),
            (4, 5, 6)
        ),
        (
            (1, 2, 3),
            (4, 5, 6)
        )
    )
)

# Display the complete 3D array
print(multiD)

# Display 3D array
for i in multiD.flat:
    print(i)

# Display each element of the 3D array
for i in range(len(multiD)):
    for j in range(len(multiD[i])):
        for k in range(len(multiD[i][j])):
            print(multiD[i][j][k])