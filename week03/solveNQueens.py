class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board
        
        def dfs(row: int):
            # terminator
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else: # precess current level
                for i in range(n):
                    # pruning
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue  
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    # drill down (if one is checked in current row, drill down to next row immediately)
                    dfs(row + 1)
                    # reverse current status
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        
        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set() 
        diagonal2 = set()
        row = ["."] * n
        dfs(0)
        return solutions
