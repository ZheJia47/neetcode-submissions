class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for item in strs:
            encoded_string += str(len(item)) + '#' + item
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter_idx = s.find('#', i)
            length = int(s[i:delimiter_idx])
            start = delimiter_idx + 1
            result.append(s[start:start + length])
            i = start + length
        return result