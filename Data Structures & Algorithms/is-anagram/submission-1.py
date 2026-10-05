class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort=[i for i in s]
        s_sort.sort()

        t_sort=[i for i in t]
        t_sort.sort()

        return s_sort==t_sort