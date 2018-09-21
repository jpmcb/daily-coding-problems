# Return K-th to last

from LinkedList import LinkedList

def last_iter(llist, k):
    if llist.head == None: return

    size = len(llist)

    counter = 0
    current = llist.head
    while size - k != counter and current != None:
        current = current.next
        counter += 1

    return current

def last_rec(llist, k):
    pass

ll = LinkedList()
print("\nTesting kth to last\n")
ll.generate(15, 0, 9)
print(ll)

print("Result:")
print(last_iter(ll, 15))