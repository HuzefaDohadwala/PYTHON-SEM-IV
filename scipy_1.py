from scipy import linalg
import numpy as np

#7x + 2y = 8
#4x + 5y = 10
a=np.array([[7,2],[4,5]])
b=np.array([8,10])
#2X2 matrix
x=np.array([[1,2],[3,4]])
#linear eqn
linear = linalg.solve(a,b)
print(linear)
#inverse of matrix
inverse = linalg.inv(x)
print(inverse)
#pseudo inverse
p_inverse = linalg.pinv(x)
print(p_inverse)
# determinant
d=linalg.det(x)
print(d)
#Singular Value Decomposition
x1 , y , z= linalg.svd(x)
print(x1,y,z)
#Eigenvalues and EigenVectors
val , vect = linalg.eig(x)
print(val , vect)
#norm
# Calculating the L2 norm
a = linalg.norm(x)
# Calculating the L1 norm
b = linalg.norm(x , 1)
print(a)
print(b)