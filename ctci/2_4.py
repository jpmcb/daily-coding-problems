# Partition

from LinkedList import LinkedList

def make_partition(llist, val):
    # generate two linked lists around the partition
    llist_a = LinkedList()
    llist_b = LinkedList()

    node = llist.head
    while(node != None):
        if node.data < val:
            llist_a.add(node.data)
        else:
            llist_b.add(node.data)
        node = node.next

    # Merge the linked lists around the partition
    llist_final = LinkedList()
    node = llist_a.head
    while(node != None):
        llist_final.add(node.data)
        node = node.next
    
    node = llist_b.head
    while(node != None):
        llist_final.add(node.data)
        node = node.next

    return llist_final

ll = LinkedList()
print("\nTesting partition\n")
ll.generate(10, 0, 9)
print(ll)
returned = make_partition(ll, 5)
print("Result:")
print(returned)