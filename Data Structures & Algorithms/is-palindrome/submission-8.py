class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()

        s_reverse = s[::-1]
        return s == s_reverse
        