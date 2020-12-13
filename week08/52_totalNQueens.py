class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return 0
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, col, pie, na):
        if row >= n:
            self.count += 1
            return
        # bits 表示当前可以放置皇后的位置，bit位用1表示空位
        # 初始时，列/撇/捺 都是0，取反后是全1.
        # 1左移n位再减1，即低N位全1，
        # 两部分相与后，只有低N位全1，即可以理解为，初始状态下，第0行的N个位置均可放置皇后。
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & (-bits) # 获取低位出现的第一个1的位置
            bits = bits & (bits - 1) # 将低位的第一个1清零，表示在这个位置放置皇后
            # DFS下探时，撇/捺相当于皇后位置左移/右移一个位置
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            # 此种传参方式没有改变 row/col/pie/na 本身，所以不需要恢复现场。

