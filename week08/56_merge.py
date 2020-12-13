class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 将interval元素按左边界排序
        intervals.sort(key = lambda x : x[0])  # sort(key, reverse=False)

        merge = []
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge
