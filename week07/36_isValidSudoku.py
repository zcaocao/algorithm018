#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_idx = (i//3)*3 + j//3
                    # 在字典中记录当前值和出现次数
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_idx][num] = boxes[box_idx].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or  boxes[box_idx][num] > 1:
                        return False
        return True

