# perkalian matriks 

"""
Simbol @ adalah operator biner di Python yang diperkenalkan 
secara resmi pada Python 3.5 melalui PEP 465. 
Operator ini khusus dirancang untuk melakukan perkalian 
matriks (matrix multiplication)
"""

import numpy as np

# Membentuk dua matriks 2X2
A = np.array([[1,2],
              [3,4]])

B = np.array([[5, 6],
              [7,8]])

# Ketika cara di bawah ini menghasilkan output yang persis sama:
C1 = A @ B
C2 = np.matmul(A, B)
C3 = A.dot(B)

# Perkalian Element-wise (*)
print("Metode: Element-wise (*)")
# [1*5, 2*6]
# [3*7, 4*8]
print(A * B)
"""
Output:[[5, 12]
        [21 32]]
"""

# Perkalian Matriks (@)
print("\nMetode: Matriks (@)") 
# [(1*5 + 2*7), (1*6 + 2*8)]
# [(3*5 + 4*7), (3*6 + 4*8)]
print(C3)
"""
Output:[[19, 22]
        [43, 50]]
"""
