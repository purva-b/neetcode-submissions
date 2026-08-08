class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(ch for ch in s if ch.isalnum())
        strcop = s[::-1]
        if strcop.lower() == s.lower():
            return True
        return False