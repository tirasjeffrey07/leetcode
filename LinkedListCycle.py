"""
Given a LL return true if it has a cycle else return false

A cycle is when a link from one node loops back to another preexisting node

[1] -> [2] -> [3] -> [4]
        ^             |
        |             |
        |             |
        ---------------

there are two approaches to this:
1) Using a Hashset to keep track of visited nodes -  O(N) Time and O(N) space        
2) Use Floyd's Turtle and Hare -  O(N) Time and O(1) space        


I used the second method here:

- have two pointers slow and fast
- slow moves one node ahead
- fast moves two nodes ahead
- initially both start at the first node
- at some point, if there's a cycle, fast will meet slow to overtake it since fast is twice as fast as slow
- it is O(N) coz at any given arbitrary length fast will catch slow (if a cycle exists) within N iterations/skips
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: [ListNode]) -> bool:
        fast = head
        slow = head

        # empty list has no cycle
        if head == None:
            return False
        
        # fast is the first node that will reach the end if theres no cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
