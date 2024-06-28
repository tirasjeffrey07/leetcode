"""
Given an array, find the kth largest element
NOT THE KTH DISTINCT ELEMENT

nums = [6,3,4,5,5,1,1,2], k = 3
returns 5

1st 2nd 3rd
6,  5,  5

nums = [1,1,1,1,1,1,1,1,2], k = 5
returns 1



Approaches:

1) Min heap
2) Max Heap O(N logK)
3) QuickSelect (least efficient way) O(N^2) worst case and O(N) avg case


In this code I am implementing max heap. So how do you do it?

The main property of max heap is that the top most element will always have the largest element in the heap

Each time we remove an element from the heap, the heap needs to be heapified to retain the max heap property

So we pop k times and return the Kth largest element

"""

import heapq

def findKthLargest(self, nums: list[int], k: int) -> int:
    # python only support minheap 
    # negate all the elements to get the same functionality
    for i in range(len(nums)):
        nums[i] = -nums[i]
    
    # inplace heapify
    heapq.heapify(nums)

    # pop the max element k - 1 times
    for _ in range(k - 1):
        heapq.heappop(nums)

    # return the kth element being popped
    return -heapq.heappop(nums)