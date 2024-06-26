
"""
Given the head of a linked list, return True if its a palindromic sequence

"""


def isPalindrome( head) -> bool:
    """
    s = []
    ptr = head                       # easy
    while ptr:                       # naive solution
        s.append(ptr.val)
        ptr = ptr.next

    return s == s[::-1]
    """
    # optimal linear time & constant space solution
    # move fast to the end, slow to the mid by using Floyd's Turtle and Hare
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    # reversing from slow to the end ie latter half of the LL
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    # after reversing, iterate from both ends
    left = head
    right = prev

    while right:
        if right.val != left.val:
            return False
        left = left.next
        right = right.next
    return True