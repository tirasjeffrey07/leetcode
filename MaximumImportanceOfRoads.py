"""
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.



------------------------------------------------------------------------------
Example 1:

Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43

Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.
------------------------------------------------------------------------------
Example 2:

Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20

Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.
------------------------------------------------------------------------------


Thought process:

So, we are given 
- n (number of nodes/cities) 
- roads (edges)

we are asked to assign values to the 'n' nodes (cities) from 0 to n - 1
So that the importance (sum) upto to the maximum

How do we calculate the importance? 
take nodes n1 and n2, the importance of the road connecting node and node 2 is
value of node1 + value of node2

So our job is to assign the values (1-n) in such a way that the importance is maximised...


How do we do this?

Consider the example...

roads = [[0,1], [1,2]]

        0-------1
                |
                |
                |
                2

n = 3, so we assign 0,1,2 to 3 of the nodes

- In the above diagram (which is like the letter L, with nodes on each of the 3 points)
- say we assign values 0 to node 0, 1 to node 1, 2 to node 2
- Let us calculate the sum (total importance)
    sum => 0 + 1 (edge1/road1) + 
        1 + 2 (edge2/road2)
        => 4
        
        0         1
        0-------1
                |
                |
                |
                2  2

- we can do better,,, but how?
- notice the number of edges(roads) each node(city) has... node 0 has 1 edge, node 1 has 2 edges, node 2 has 1 edge
- so we assign the highest value to the node with the most edges, then the second highest value to the node with the second highest number of edges and so on... 
- we assign, the highest value (2) to node 1, we assign value 1 to node 0, value 0 to node 2
- hence our sum = (1 + 2) + (2 + 0) = 5 (maximum possible value)

            
        0         2
        0-------1
                |
                |
                |
                2  1


This is a greedy solution,
we sort the node based on the count of edges (in and out)
we assign the highest to the node w highest count 
"""

from collections import List

def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    # greedy algo
    # we assign the biggest values to the nodes with most edges
    # that way we get the highest sum

    # index 'node' will contain the count of 'node' in roads
    edgeCount = [0] * n

    # count in's and out's of each road and increment the array accordingly
    for node1, node2 in roads:
        edgeCount[node1] += 1
        edgeCount[node2] += 1

    res = 0
    value = 1 # the value we assign to the nodes

    # calculating importance = count of edges for a node * value assigned tothe node 
    for count in sorted(edgeCount):
        res += count * value
        value += 1
    
    return res