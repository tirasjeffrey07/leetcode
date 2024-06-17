"""

Leetcode 38

Given the head of a sorted linked list, remove all the duplicates and return the sorted LL

sample ip
1 1 2 3 3

sample op
1 2 3

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head) -> ListNode:
    # empty node edge case
    if head is None:
        return

    # temp is find duplicates and pass them
    # ptr is to skip the duplicates 
    ptr, temp = head, head

    while temp.next is not None:
        # since there might be multiple duplicates, 
        # we use temp to traverse all the duplicates
        if temp.val == temp.next.val:
            temp = temp.next
        
        # if the next value is different from the current value
        else:
            # link the ptr to non-duplicate value 
            ptr.next = temp.next
            # move ptr and temp to the non-duplicate value
            ptr = temp.next
            temp = temp.next
    
    # at this point, temp.next is None ie end of list
    # so we link ptr to None and end the list
    ptr.next = temp.next
    
    return head