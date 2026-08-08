class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(ch for ch in s if ch.isalnum())
        if (s[::-1]).lower() == s.lower():
            return True
        return False