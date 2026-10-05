class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            sorted_s=sorted(s)
            sorted_str=''.join(sorted_s)
            if sorted_str not in d:
                d[sorted_str]=[s]
            else:
                d[sorted_str]+=[s]
        return list(d.values())