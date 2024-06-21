def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sortedStr = str(sorted(s))
            if sortedStr in hashmap:
                hashmap[sortedStr].append(s)
            else:
                hashmap[sortedStr] = [s]
        return list(hashmap.values()) 