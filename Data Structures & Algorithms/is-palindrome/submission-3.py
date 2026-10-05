class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        reversed_cleaned=''.join(reversed(cleaned))

        return cleaned == reversed_cleaned


