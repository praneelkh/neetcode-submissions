class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = ""
        for char in s:
            if char.isalnum():
                revStr += char.lower()
        return revStr == revStr[::-1] 