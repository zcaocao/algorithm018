class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queen, xy_diff, xy_sum):
            p = len(queen)
            if p == n:
                result.append(queen)
                return None
            for q in range(n):
                if q not in queen and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queen+[q], xy_diff+[p-q], xy_sum+[p+q])
            
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

        '''
        DFS时直接将皇后所在列，撇，捺的列表当作参数传递
        皇后每行只能有一个，每列也只能有一个。
        每一次累计当前行的皇后所在的列标[q]，所在撇标[p-q]，所在捺标[p+q]，带入下一层递归。
        打印棋盘时，遍历result里的子list，其实每个子list只记录的某行的皇后所在列标，因此只有一个数字。
        因为行列标计数都是从0开始，所以，刚好"Q"前有i个"."， 插入"Q", "Q"后有 n-i-1 个"."。
        '''
