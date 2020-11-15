class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[left]:
            return nums[0]
        
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
