# Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two numbers appear in two linked lists
# For example,
# [2, 4, 3]
# [5, 6, 4]
# should result in [7, 0, 8]
# or in other words, 342 + 465 = 807
# Note that carrying is required.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # First node for list to be returned.
        sentinal = ListNode(0)
        x = sentinal
        carry = 0
        
        # As long as the nodes are not null ...
        while l1 or l2:
            v1 = v2 = 0
                
            if l1:
                v1 = l1.val
                l1 = l1.next
                
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            sum = v1 + v2 + carry
            
            if sum > 9: 
                carry = 1
            else:
                carry = 0
            
            x.next = ListNode(sum % 10)
            x = x.next
            
        # Does the last number need to be 1?
        if carry:
            x.next = ListNode(1)
        
        # Just return the "next" of the sentinal since this solution relies on
        # not having to allocate the "current" node in the list
        return sentinal.next

