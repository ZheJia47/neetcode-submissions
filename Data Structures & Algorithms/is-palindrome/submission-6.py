class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''.join([i.lower() for i in s if i.isalnum()])
        s2=''.join(reversed(s1))
        return s1==s2