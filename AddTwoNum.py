"""class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, val=0, next=None):
        newNode = Node(val)
        self.val = val
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = None
        self.val = val

    def addFront(self, val=0):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # used to store the answer
        dummy = ListNode()
        currentNode = dummy

        carryOver = 0
        # if l1 is not empty or l2 is not empty or carry != 0
        while l1 or l2 or carryOver:
            # extracting value from the node if it exists 
            # ie != None else set it to 0 to make it easy to add
            
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
                
            val = val1 + val2 + carryOver 
            carryOver = val // 10    # getting first digit
            val = val % 10                       # getting last digit

            # newNode = ListNode(val)
            # currentNode.next = newNode 
            # the below code is same as the above
            currentNode.next = ListNode(val)

            # traverse to the next nodes
            currentNode = currentNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
"""
Attempt 1


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # used to store the answer
        l3 = LinkedList()
        carryOver = 0
        sum = 0
        while True:
            if l1.next != None and l1.next != None:
                value = (l1.val + l2.val) % 10
                carryOver = (l1.val + l2.val) // 10
                # storing answer in l3 node
                l3.val = value + carryOver
                # move to the next node
                l1, l2 = l1.next, l2.next

            elif l1.next == None and l2.next != None:
                value = (l1.val + l2.val) % 10
                carryOver = (l1.val + l2.val) // 10
                # storing answer in l3 node
                l3.val = value + carryOver
                l2 = l2.next

            elif l1.next != None and l2.next == None:
                value = (l1.val + l2.val) % 10
                carryOver = (l1.val + l2.val) // 10
                # storing answer in l3 node
                l3.val = value + carryOver
                l1 = l1.next

            if l1.next == None and l2.next == None:
                value = (l1.val + l2.val) % 10
                carryOver = (l1.val + l2.val) // 10
                # storing answer in l3 node
                if carryOver > 0:
                    l3.val = value + carryOver
                    break

            if l1.val == 0 and l2.val == 0:
                l3.val = carryOver

            l3.addFront()
            l3 = l3.next

"""