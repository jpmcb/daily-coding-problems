def insert_sort(A):
    for i in range(len(A)):
        cur = i

        for j in range(i, len(A)):
            if A[cur] >= A[j]:
                cur = j

        A[i], A[cur] = A[cur], A[i]

A1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
insert_sort(A1)
print(A1)

A2 = [9, 1, 7, 2, 5, 4, 3, 2, 1]
insert_sort(A2)
print(A2)