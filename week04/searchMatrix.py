class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            piovt_ele = matrix[pivot_idx // n][pivot_idx % n]
            if piovt_ele == target:
                return True
            if piovt_ele > target:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
        return False
