def bubble_sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

A1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(A1)
print(A1)

A2 = [9, 1, 7, 2, 5, 4, 3, 2, 1]
bubble_sort(A2)
print(A2)