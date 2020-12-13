class Solution:
    '''
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
    '''

    def mergesort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        cnt = self.mergesort(nums, left, mid) + self.mergesort(nums, mid + 1, right)
        '''
        i, j = left, mid+1
        while i <= mid:
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            cnt += j - (mid + 1) # mid+1到j之前都可以与i构成翻转对(不包括j)，因为 >
            i += 1
        self.merge(nums, left, mid, right)
        '''
        # 边统计翻转对数，边排序合并。
        i, t = left, left
        temp = []
        for j in range(mid+1, right+1):
            while i <=mid and nums[i] <= 2 * nums[j]: i += 1
            while t <= mid and nums[t] < nums[j]: 
                temp.append(nums[t])
                t += 1
            temp.append(nums[j])
            cnt += mid - i + 1 # i到mid都可以和j构成翻转对(包括i)，因为 <=
        while t <= mid: 
            temp.append(nums[t])
            t += 1
        nums[left:right+1] = temp
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        return self.mergesort(nums, 0, len(nums)-1)


