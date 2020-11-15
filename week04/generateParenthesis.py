class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(tmp, left, right):
            if len(tmp) == 2 * n:
                res.append(''.join(tmp))
                return
            if left < n:
                tmp.append('(')
                dfs(tmp, left + 1, right)
                tmp.pop()
            if right < left:
                tmp.append(')')
                dfs(tmp, left, right + 1)
                tmp.pop()

        dfs([], 0, 0)
        return res
