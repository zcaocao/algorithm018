class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O":
                return
            
            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
