class Solution:
    '''
    计数排序：
    1.遍历arr1，先生成出现频率统计数组freq[](此处有空间优化)；
    2.遍历arr2, 遇到x在freq中，将frq[x]个x加入到返回值数组，遍历结束时，arr1中包含所有的arr2的元素已有序；
    3。最后遍历freq，将剩余元素按序按个数填入返回数组尾部。
    '''
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        freq = [0] * (upper + 1)
        res =[]
        for x in arr1:
            freq[x] += 1

        for x in arr2:
            res.extend([x] * freq[x])
            freq[x] = 0

        for x in range(upper + 1):
            if freq[x] > 0:
                res.extend([x] * freq[x])
        return res
