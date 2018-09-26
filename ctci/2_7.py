# Intersection

def intersect(llist1, llist2):

    # Check that their tails are at least the same
    if llist1.tail != llist2.tail:
        return False

    # get the shorter of the two
    shorter = llist1 if len(llist1) < len(llist2) else llist2
    longer = llist1 if len(llist1) >= len(llist2) else llist2

    # Check the difference in lengths between the nodes 
    diff = len(longer) - len(shorter)

    # Get the current nodes
    shorter_curr = shorter.head
    longer_curr = longer.head

    # Chop off the excess in the longer one
    for _ in range(diff):
        longer_curr = longer_curr.next

    # Go through the nodes sequentially untill the intersection is reached
    # We don't have to check for none, because their tails are the same,
    # so we at least know that their tails are the same 
    while shorter_curr != longer_curr:
        shorter_curr = shorter_curr.next
        longer_curr = longer_curr.next

    return longer_curr