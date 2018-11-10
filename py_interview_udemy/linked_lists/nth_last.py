# Write a function that takes a head node and an 
# integer value n and then returns the nth to 
# last node in the linked list. For example, given:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def nth_to_last(x, ll):
    right = ll
    left = ll
    d1 = 0
    d2 = 0

    # Send the first runner to the end of the LL
    # Track the distance as we go
    while right.next != None:
        right = right.next
        d1 += 1

    # Advance the next runner until we have reached 
    # the nth designated node
    while x != (d1 - d2):
        left = left.next
        d2 += 1

    return left
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

returned = nth_to_last(1, a)
print(returned.value)