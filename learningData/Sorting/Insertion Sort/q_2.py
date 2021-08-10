"""
EASY
----------
ADD TWO 4-BIT BINARY INTEGERS STORED IN 4-ELEMENT ARRAYS, 'A' AND 'B'
AND STORE THE RESULT IN ANOTHER 5-BIT ARRAY 'C'
A = [1, 0, 1, 1] # 11
B = [1, 1, 1, 1] # 15
C = [?, ?, ?, ?, ?] # A + B => 11 + 15 = ?
"""
import math

def Add(a, b):
    c = [0, 0, 0, 0, 0]
    carry = 0
    for i in range(0, len(a)):
        c[i] = math.floor((a[i] + b[i] + carry) % 2)
        carry = math.floor((a[i] + b[i] + carry) / 2)
    print(carry)
    print(i)
    c[i+1] = carry
    
    return c



A = [0, 0, 1, 1]
B = [1, 0, 1, 1] 

a = [1, 1, 1]

print(f"Adding {A}, and {B}")
print(Add(A, B))
print(f"Adding {a} and {a}")
print(Add(a, a))

