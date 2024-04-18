# To print L and U matrix
import numpy as np
from scipy.linalg import lu
#add the library to import lu
A = np.array(eval(input()))
#add the code to get the L and U matrix
p,l,u = lu(A)
print(l)
print(u)
# To print X matrix (solution to the equations)
import numpy as np
from scipy.linalg import lu_factor , lu_solve
#add the library to import lu_factor, lu_solve
A = np.array(eval(input()))
b = np.array(eval(input()))
#add the code to get the solution of the matrix
l,p = lu_factor(A)
x = lu_solve((l,u),b)
print(x)
