class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # initializes every value to be a list in the dict
        for string in strs: # iterate through each string
            charCount = self.findCharFreqTuple(string) # find the character tuple that corresponds to this string
            result[charCount].append(string) # append the string to the list of strings for this character tuple
        return list(result.values()) # problem wants list[list[str]]


        
    def findCharFreqTuple(self, s: str) -> tuple: # tuple b/c list is not a valid key type
        res = [0] * 26 # since we are dealing w/ lowercase english letters the array can be fixed
        for char in s:
            idx = ord(char) - ord('a') # logic to make 0 index correspond w/ 'a'
            res[idx] += 1
        return tuple(res)