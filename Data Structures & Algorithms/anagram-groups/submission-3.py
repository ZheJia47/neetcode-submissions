class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            s1=sorted(s)
            s2=''.join(s1)
            if s2 not in d:
                d[s2]=[s]
            else:
                d[s2]+=[s]
        return list(d.values())