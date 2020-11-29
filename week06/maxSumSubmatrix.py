class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")  # 记录过程中最接近k的子序和，最后一次的值即为返回值
        # 固定左边界，先求各种左右边界组合下，行元素的累加和
        for left in range(col):
            sum_list = [0] * row
            for right in range(left, col): # 移动右边界
                for j in range(row):
                    sum_list[j] += matrix[j][right] # 按列存储的，每次right变化时，累加隔壁行的元素（前缀和）
                # 在left和right边界下的矩阵中， 求最大子序（子矩阵）和 不超过K 的 值。
                # 在已有行前缀和的基础上，继续累加各行的和，进而求矩阵和。
                # 给定子序和k，与数组子序和的关系变换：
                # 在下标为（0-j）的数组中，下标i和下标j之间的子序和可以表示为：sum[i,j] = sum[0,j] - sum[0,i-1] 
                # 如果限定sum[i,j] <= k, 也就是 sum[0,j] - sum[0,i-1] <= k
                # 进而转换成 sum[0,j] - k <= sum[0,i-1]
                # 初始化一个cur，代表当前累加的行和 （也就是当前子矩阵和）
                # 再初始化一个数组arr，记录排序后的sum[0,i-1]们，
                # 遍历行累加和数组 sum_list, 计算每累加一行后的矩阵和，也就是cur 
                # 每一个cur都要加入arr，也就是组成sum[0,i-1]的过程。
                # 但是，在加入arr之前，要先判断这个cur，现有arr里的元素，以及k，是否满足上面变换后的关系。
                # 也就是 cur - arr[某个元素] <= k, (这里 arr[某个元素]也就是上面提及的某个sum[0,i-1])
                # （由 cur - arr[某个元素] <= k 推导出 cur - k <= arr[某个元素]）
                # 借助bisect，来判断 cur-k 是否在arr现有范围中，如果有效，就返回比 cur-k 大的那一个的位置下标（可能存在多个，只找最小的）       
                # 找到最小的arr元素位置后，cur - arr[loc] 就是这一轮遍历求得的有效子序和。然后跟当前最大res比较再更新。
                # res = max(cur-arr[loc], res) 
                # 以下代码：
                arr = [0]
                cur = 0
                for tmp in sum_list:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): 
                        res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res

        

