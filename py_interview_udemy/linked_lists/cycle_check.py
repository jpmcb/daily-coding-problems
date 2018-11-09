# Given a singly linked list, write a function which 
# takes in the first node in a singly linked list 
# and returns a boolean indicating if the linked list 
# contains a "cycle".

# A cycle is when a node's next 
# point actually points back to a previous 
# node in the list. This is also sometimes known as a 
# circularly linked list.

# You've been given the Linked List Node class code:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cycleCheck(ll):
    runner1 = ll
    runner2 = ll 

    # Go until the end of the LL
    while runner1 != None and runner2 != None:
        try:
            runner1 = runner1.next.next
            runner2 = runner2.next
        except AttributeError:
            runner1 = None
        
        if runner1 == runner2:
            return True

    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z


print(cycleCheck(a))
print(cycleCheck(x))