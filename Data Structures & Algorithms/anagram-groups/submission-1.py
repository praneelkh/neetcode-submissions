class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visitedMap = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in visitedMap:
                visitedMap[sort] = [s]
            else:
                visitedMap[sort].append(s)
        return list(visitedMap.values())
        