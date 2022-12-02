class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            Solution.rotateRing(matrix, i)

    def rotateRing(matrix, i):
        for row, col in Solution.getIndices(matrix, i):
            Solution.rotateCell(matrix, row, col)

    def getIndices(matrix, i):
        return [[i, col] for col in range(i, len(matrix) - i - 1)]

    def rotateCell(m, r, c):
        n = len(m)
        m[r][c], m[c][n-1-r], m[n-1-r][n-1-c], m[n-1-c][r] = m[n -
                                                               1-c][r], m[r][c], m[c][n-1-r], m[n-1-r][n-1-c]
