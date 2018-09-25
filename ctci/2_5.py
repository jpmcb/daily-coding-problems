# Sum List

from LinkedList import LinkedList

def sumList(ll_a, ll_b):
    # problem variables
    carry = 0
    value = 0

    current_a = ll_a.head
    current_b = ll_b.head

    ll = LinkedList()

    # Go through both linked lists sequentially adding as we go
    while(current_a != None or current_b != None):
        if current_a != None:
            value += current_a.data
            current_a = current_a.next

        if current_b != None:
            value += current_b.data
            current_b = current_b.next

        # Add appropriate value to new LL and make carry as needed
        ll.add((value + carry) % 10)
        carry = 1 if value >= 10 else 0
        value = 0

    return ll
        



ll_a = LinkedList([7, 1, 6])
print(ll_a)
ll_b = LinkedList([5, 9, 2, 3, 2, 1])
print(ll_b)
print(sumList(ll_a, ll_b))