class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        r1=[[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                r1[j][n-1-i]=matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j]=r1[i][j]