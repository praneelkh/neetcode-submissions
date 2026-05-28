class Solution:
    # prefix each word with following string length + symbol as delimiter 
    # for example 5#hello5#world
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + word_length])
            i = j + 1 + word_length
        return decoded
