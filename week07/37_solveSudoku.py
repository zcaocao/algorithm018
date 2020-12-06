class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 初始化 行，列，块的剩余可用数字，每个位置都可以是1-9的数字,9行，9列，9块
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        #print(row)

        # 遍历board并收集需要填充数字的位置，记录到empty
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    # 在行/列/块可用数字集合中清除该数字
                    row[i].remove(val) 
                    col[j].remove(val)
                    block[(i//3)*3 + j//3].remove(val)
                else:
                    empty.append((i, j))

        def dfs(iter = 0):
            # terminator empty处理完，表示得到答案
            if iter == len(empty): 
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j //3
            # 合并集合 行/列/块 当前可用的数字， 并遍历
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(iter + 1):
                    return True
                # 上面路不通，则回溯
                row[i].add(val)  
                col[j].add(val)
                block[b].add(val)
            return False

        dfs()    


