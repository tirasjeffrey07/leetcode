"""
Leetcode 997 

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1) The town judge trusts nobody.
2) Everybody (except for the town judge) trusts the town judge.

There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

"""

from collections import defaultdict


def findJudge(n: int, trust: list[list[int]]) -> int:
    incoming, outgoing = defaultdict(int), defaultdict(int)

    for a, b in trust:
        incoming[b] += 1
        outgoing[a] += 1
    print(incoming, outgoing)
    for i in range(1, n + 1):
        if outgoing[i] == 0 and incoming[i] == n - 1:
            return i
    return -1


print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
