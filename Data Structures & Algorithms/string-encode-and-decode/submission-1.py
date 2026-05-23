class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str
            
    def decode(self, s: str) -> List[str]:
        res, ptr1 = [], 0
        while ptr1 < len(s):
            ptr2 = ptr1
            while s[ptr2] != '#':
                ptr2 += 1
            length = int(s[ptr1:ptr2])
            res.append(s[ptr2 + 1 : ptr2 + 1 + length])
            ptr1 = ptr2 + 1 + length
        return res

    
