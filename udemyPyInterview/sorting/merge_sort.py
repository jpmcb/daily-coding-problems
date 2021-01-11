def merge(A, l, r):
    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            A[k] = l[i]
            i += 1
        else:
            A[k] = r[j]
            j += 1

        k += 1

    while i < len(l):
        A[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        A[k] = r[j]
        j += 1
        k += 1

def merge_sort(A):
    if len(A) > 1:
        m = len(A) // 2
        l = A[:m]
        r = A[m:]

        merge_sort(l)
        merge_sort(r)

        merge(A, l, r)

A1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(A1)
print(A1)

A2 = [9, 1, 7, 2, 5, 4, 3, 2, 1]
merge_sort(A2)
print(A2)