class Solution:
    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right+1] = temp

    def mergesort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2

        cnt = self.mergesort(nums, left, mid) + self.mergesort(nums, mid + 1, right)
        i, j = left, mid + 1
        while i <= mid:
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            cnt += j - (mid + 1)
            i += 1
        self.merge(nums, left, mid, right)
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        return self.mergesort(nums, 0, len(nums)-1)
