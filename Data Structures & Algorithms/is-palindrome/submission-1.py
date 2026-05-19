class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_text = ''.join(char for char in s if char.isalnum())
        
        
        i = 0
        j = -1 

        while i < len(clean_text) and j < len(clean_text):
            if clean_text[i] != clean_text[j]:
                return False
            elif i == j:
                return True
            else:
                i += 1
                j -= 1
        return True    