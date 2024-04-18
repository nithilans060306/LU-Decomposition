# LU Decomposition 

## AIM:
To write a program to find the LU Decomposition of a matrix.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Moodle-Code Runner

## Algorithm
1. Define the package as scipy.linalg import lu.
2. Get input from user and print L and U matrix by 'print' .
3. Define a package as "from scipy.linalg import lu_factor, lu_solve" and create the variable as 'X' include the package in that variable.
4. print the variable 'X'

## Program:
(i) To find the L and U matrix
```python
import numpy as np
from scipy.linalg import lu
n = np.array(eval(input()))
p,l,u = lu(n)
print(l)
print(u)
```
(ii) To find the LU Decomposition of a matrix
```python
import numpy as np
from scipy.linalg import lu_factor , lu_solve
a = np.array(eval(input()))
b = np.array(eval(input()))
l,p = lu_factor(a)
x = lu_solve((l,p),b)
print(x)
```
## Output:
![Exp5_1](image.png)
![Exp5_2](image-1.png)

## Result:
Thus the program to find the LU Decomposition of a matrix is written and verified using python programming.

