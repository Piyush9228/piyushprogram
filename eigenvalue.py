import numpy as np
import sympy as sy
l=sy.symbols("lambda")
A=np.array([[1,2],[3,2]])
I=sy.eye(2)
z=A-l*I
sy.pprint(z)
y=np.linalg.eigvals(A)
print("Eigen values",y)