# leet 1347
# find the minimum number of steps required to convert a given string into the anagram of another string
# eg: bab and aba
# one replacement of either the first a or the last a 
# to convert it to bba or abb, both of which are anagrams of bab
# anagram of a string is the same string with different or same ordering of letters

# convert t into an anagram of s if its not an anagram already


def minSteps( s: str, t: str) -> int:
    # a string is an anagram of itself
    if s==t:
        return 0
    for letter in t:
        indexList = [letter,s.count(letter)]
    print(indexList)
    
print(minSteps("bab;","aab"))


