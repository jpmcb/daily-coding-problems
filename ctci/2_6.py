# Palindrome

from LinkedList import LinkedList

# Work in progress, reverse linked list to see if it's the same
def reverse(llist):
    pass

# Using a stack, as we progress the Linked List, push to stack
# Pop off once middle is reached (accomidates for special case even and odd)
def using_stack(llist):
    stack = []

    inMiddle = False
    current = llist.head
    runner = llist.head
    while(current != None):
        if inMiddle:
            if current.data != stack[len(stack) - 1]:
                return False
            stack.pop()
            current = current.next
        else:
            # Check if list was odd
            runner = runner.next
            if runner == None:
                inMiddle = True
            else:
                # check if list was even
                runner = runner.next
                if runner == None: 
                    inMiddle = True
                stack.append(current.data)
            
            current = current.next

    return True


# ----------
# Test cases

ll = LinkedList([0, 1, 2, 1, 0])
print(ll)
print(using_stack(ll))

ll = LinkedList([0, 1, 2, 2, 1, 0])
print(ll)
print(using_stack(ll))

ll = LinkedList([0, 1, 2, 2, 3, 0])
print(ll)
print(using_stack(ll))

ll = LinkedList([0, 3, 2, 1, 0])
print(ll)
print(using_stack(ll))