# Returns the index of the element (or where the element should be inserted)
def bin_search(A, x):
    l = 0
    r = len(A) - 1
    m = None

    while l <= r:
        m = (l + r) // 2
        #print('mid: ', m)

        if A[m] == x:
            return m
        
        elif A[m] > x:
            r = m - 1

        elif A[m] < x:
            l = m + 1
            
    return m

print(bin_search([1, 2, 3, 4, 5], 4))
print(bin_search([1, 2, 3, 4, 5], 1))
print(bin_search([1, 2, 3, 4, 5], 5))

print(bin_search([0, 1], -1))

print(bin_search([], 1))