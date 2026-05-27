class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # initializes every value to be a list in the dict
        for string in strs:
            charCount = self.findCharFreqTuple(string)
            result[charCount].append(string)
        return list(result.values())


        
    def findCharFreqTuple(self, s: str) -> tuple:
        res = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            res[idx] += 1
        return tuple(res)