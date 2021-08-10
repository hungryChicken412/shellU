"""
VERY EASY
----------
SORT THIS SIMPLE ARRAY
A = [1, 3, 6, 3, 4]
"""


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    j = 0
    i = 0
    k = p

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def MergeSort(A, p, r):
    if p < r:
        q = (p + (r-1))//2
        
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)

        return A

    

A = [1, 3, 6, 3, 4]
B = [12, 11, 13, 5, 6]
C = [10, 5, 13, 8, 2]

print(MergeSort(A, 0, 4))
print(MergeSort(B, 0, 4))
print(MergeSort(C, 0, 4))
