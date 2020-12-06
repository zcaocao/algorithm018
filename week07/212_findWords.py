class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if END_OF_WORD in cur_dict:
                self.result.add(cur_word)
            tmp, board[i][j] = board[i][j], '@'
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
                    dfs(board, x, y, cur_word, cur_dict)
            board[i][j] = tmp

        if not board or not board[0]: return[]
        if not words: return []
        self.result = set()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        END_OF_WORD = "#"

        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    dfs(board, i, j, "", root)
        return list(self.result)

        


