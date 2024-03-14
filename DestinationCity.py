"""
Leet 1436
--------------------
Destination City
--------------------

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

"""


def destCity(paths: list[list[str]]) -> str:
    source, dest = [], []

    for i in range(len(paths)):
        source.append(paths[i][0])
        dest.append(paths[i][1])
    
    # elements in set a that are not in set b => set(dest) - set(source)
    for x in (set(dest) - set(source)):
        return x

"""
    for i in range(1,len(flattened),2):
        source.append(flattened[i])
        print(flattened[i],sep=" ")
    print()

    for i in range(0,len(flattened)-1,2):
        dest.append(flattened[i])
        print(flattened[i],sep=" ")
    
    print(source, dest)
"""

print(destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
