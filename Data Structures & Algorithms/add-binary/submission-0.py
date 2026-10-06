class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        carry=0
        i,j = len(a)-1, len(b)-1

        while i>=0 or j>=0 or carry:
            if i>=0:
                carry += ord(a[i])-ord('0')
                i-=1
            if j>=0:
                carry += ord(b[j])-ord('0')
                j-=1

            res.append(str(carry%2))
            carry//=2

        return ''.join(reversed(res))
