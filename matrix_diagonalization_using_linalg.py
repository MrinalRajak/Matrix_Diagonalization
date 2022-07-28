

# Matrix operation using numpy(linalg) and Diagonalization

import numpy as np
import numpy.linalg as lin

a=np.array([])
n=int(input("Enter the order of the matrix: "))
a=np.append(a,[int(input())for i in range(n**2)])
a.shape = (n,n)

print("The matrix is:\n",a)

print("\nDeterminant of a")
print(np.round(lin.det(a),3)) # For three decimal places

print("\nThe Inverse of a")
print(np.round(lin.inv(a),3))

print("\nThe product of a and a_inv")
print(np.dot(a,lin.inv(a)))

eigenvalues,eigenvectors = lin.eig(a)
print("\nThe eigenvalues are")
print(eigenvalues)
print("\nThe eigenvectors are")
print(eigenvectors)
print("\nThe eigenvectors belonging to the 1st eigenvalues")
print(eigenvectors[:,0])
print("\nThe eigenvectors belonging to the 2nd eigenvalues")
print(eigenvectors[:,1])
print("\nThe Inverse of the eigenvector matrix")
inv_eigenvector = lin.inv(eigenvectors)
print(inv_eigenvector)
print("\nThe Diagonal matrix")
Diagonal_matrix=inv_eigenvector.dot(a).dot(eigenvectors)
print(Diagonal_matrix)

