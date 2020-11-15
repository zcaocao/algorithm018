class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        kid = 0
        i = 0
        for ss in s:
            if i == len(g):
                break
            if g[i] <= ss:
                kid += 1
                i += 1
        return kid
