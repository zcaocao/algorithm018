class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dict = collections.Counter(nums)
        heap = [(-val, key) for key, val in dict.items()]
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
