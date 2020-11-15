class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(i + nums[i], rightmost)
                if rightmost >= n -1:
                    return True
        return False
