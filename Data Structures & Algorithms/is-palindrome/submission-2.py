class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_valid=True

        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        reversed_cleaned=''.join(reversed(cleaned))

        for i in range(len(cleaned)):
            if cleaned[i] != reversed_cleaned[i]:
                is_valid=False
                break

        return is_valid


