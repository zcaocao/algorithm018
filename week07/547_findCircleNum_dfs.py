class Solution:
    ''' DFS '''
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(M, visited, i):
            for j in range(N):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)
        
        N = len(M)
        count = 0
        visited = [0 for _ in range(N)]
        for i in range(N):
            if visited[i] == 0:
                dfs(M, visited, i)
                count += 1
        return count
