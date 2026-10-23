class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i, item in enumerate(temperatures):
            while stack and item > stack[-1][1]:
                stackIndex, stackItem =stack.pop()
                res[stackIndex]=i-stackIndex

            stack.append([i,item])

        return res