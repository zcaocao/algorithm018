class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        # 多一行和一列，以省去i=0或j=0的判断处理
        dp = [[0] * (col + 1) for _ in range(row +1 )]
        maxside = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    maxside = max(maxside, dp[i+1][j+1])
        return maxside * maxside
