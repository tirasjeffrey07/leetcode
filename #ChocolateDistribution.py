"""
Refer GFG

Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
1) Each student gets one packet.
2) The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

Examples:
1)
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

2)
Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 
pick the sequence 3,4,7,9,9
9-3 = 6

"""


def distribute(packets, m) -> int:
    minValue = float("inf")
    packets.sort()
    for i in range(len(packets) - m):
        minValue = min(minValue, packets[i+m - 1] - packets[i])
    return minValue


print(distribute([3, 4, 1, 9, 56, 7, 9, 12], 5))