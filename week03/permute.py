class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs (index):
            # terminetor
            if index == n:
                res.append(nums[:])
                return
            # process current level
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                # drill down
                dfs(index + 1)
                # reverse current level status
                nums[i], nums[index] = nums[index], nums[i]
            
        n = len(nums)
        res = []
        dfs(0)
        return res
