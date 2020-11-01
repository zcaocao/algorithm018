class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = []
        heap = [1]
        heapq.heapify(heap)
        for _ in range(n):
            cur = heapq.heappop(heap)
            res.append(cur)
            cur1, cur2, cur3 = cur*2, cur*3, cur*5
            setheap = set(heap)
            setTmp = {cur1, cur2, cur3}
            diff = setTmp.difference(setheap)
            if diff:
                for item in diff:
                    heapq.heappush(heap, item)
        return res[-1]
