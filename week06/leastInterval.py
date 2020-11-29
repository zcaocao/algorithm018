class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c, t = collections.Counter(tasks), 0
        p = c.most_common(1)[0][1] 
        for i in c.values():
            if i == p: t += 1
        res = (p - 1) * (n + 1) + t
        return res if res >= len(tasks) else len(tasks)
