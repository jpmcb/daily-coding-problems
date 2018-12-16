import collections as c
import heapq

s = 'tree'

# Will count the number of chars in the s string
d = c.Counter(s)
print(d)

l = list(s)

# Start with a list and build a heap from the list
h = [(d[char], char) for char in d]
heapq.heapify(h)

print(h)
