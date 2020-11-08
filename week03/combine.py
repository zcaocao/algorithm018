class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(index, result, subset):
            # terminator
            if len(subset) == k:
                result.append(subset[:]) # copy elements of subset not only a subset object
                return
            # process current level
            for i in range(index, n + 1):
                # pruning - left nums length is not enough for a complete subset.
                if k - len(subset) > n - i + 1:
                    break
                subset.append(i)
                # drill down
                dfs(i + 1, result, subset)
                # reverse current status
                subset.pop()

        dfs(1, result, [])
        return result       
