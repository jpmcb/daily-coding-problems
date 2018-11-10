# Write a function to reverse a Linked List in place. The function will take
# in the head of the list as input and return the new head of the list.

# You are given the example Linked List Node class:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(ll):
    current = ll
    nextnode = None
    prevnode = None

    while current:
        # Swap the pointers 
        nextnode = current.next
        current.next = prevnode
        
        # Advance the current tracker
        prevnode = current
        current = nextnode

    return prevnode

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

reverse(a)

print(c.value)
print(c.next.value)
print(c.next.next.value)