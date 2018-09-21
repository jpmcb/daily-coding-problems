# Remove dups

from LinkedList import LinkedList

# Using a hash table, iterates the table, adding as we go
# To check if element already exists in table
def remove_dup(llist):
    if llist.head == None:
        return
    
    current = llist.head
    table = {}
    table[current.data] = True

    while current.next != None:
        if current.next.data not in table:
            table[current.next.data] = True
            current = current.next
        else:
            current.next = current.next.next

    return

# uses a runner to go through table in O(n^2) time
def remove_followup(llist):
    if llist.head == None:
        return

    current = llist.head
    runner = current

    while current != None:
        while runner.next != None:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        runner = current

    return


# --------------
# Testing Code:

ll = LinkedList()

print("\nTesting hash remove\n")
ll.generate(100, 0, 9)
print(ll)
remove_dup(ll)
print("\n\nResult:\n", ll)

print("\nTesting followup\n")
ll.generate(100, 0, 9)
print(ll)
remove_followup(ll)
print("\n\nResult:\n", ll)