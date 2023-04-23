import numpy as np

matrix =np.array([
        [1,2,3],
        [3,4,5],
        [6,7,8]
])

matrix_2 = np.array([
    [9,8,7],
    [1,2,3],
    [4,3,2]])
#prints the matrix
print(matrix)
#prints the right diagonal of matrix
right_diagonal = np.diag(matrix)
print(right_diagonal)
#prints the left diagonal of matrix
left_diagonal = np.diagonal(matrix)
print(left_diagonal)
#sum of right diagonal
sum_right = np.trace(matrix)
print(sum_right)
#add two matrix
add = np.add(matrix,matrix_2)
print(add)
#multiply two matrix
multi = np.dot(matrix,matrix_2)
print(multi)
#cross product of matrix
cross= np.dot(matrix,matrix_2)-np.dot(matrix_2,matrix)
print(cross)
