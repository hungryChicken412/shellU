"""
VERY EASY
----------
SORT THIS SIMPLE ARRAY
A = [1, 3, 6, 3, 4]
"""


def InsertionSort(arr):
    for j in range(1, len(arr)): 
        key = arr[j]
        i = j-1
        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr



A = [1, 3, 6, 3, 4]
B = [12, 11, 13, 5, 6]
C = [10, 5, 13, 8, 2]

print(InsertionSort(A))
print(InsertionSort(B))
print(InsertionSort(C))
