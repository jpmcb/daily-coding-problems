# Delete middle

from LinkedList import LinkedList

# Removes a specified given node by replacing it's current
# data with the data in the next node. The next node is then 
# effectively removed.

# Note: This solution feels somewhat subversive. I find that
# although the "value" is being removed, the actual node that
# is given is not removed. But then rather, what's the 
# difference? Effectively, the lowest level memory bits are
# not removed but the high level view of what we want is.

# Note on last node: This algorithm will not work on the last
# node in the linked list. Because the next property for that
# node is null, we cannot go to the next dummy node. We could
# somehow reference this node as terminated? Maybe by giving
# the value itself a dead value None, or -1?
 
def delete_mid(node):
    if node == None or node.next == None: return False
    
    node.data = node.next.data
    node.next = node.next.next
    return True

ll = LinkedList()
print("\nTesting remove middle\n")
ll.generate(10, 0, 9)
print(ll)
delete_mid(ll.head.next.next.next)
print("Result:")
print(ll)