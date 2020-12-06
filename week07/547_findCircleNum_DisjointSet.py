class Solution:
    ''' Disjoint Set '''
    def findCircleNum(self, M: List[List[int]]) -> int:
        def _union(p, i, j):
            p1 = _parent(p, i)
            p2 = _parent(p, j)
            p[p2] = p1
        
        def _parent(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i; i = p[i]; p[x] = root
            return root
        if not M: return 0

        N = len(M)
        p = [i for i in range(N)]
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    _union(p, i, j)
        return len(set([_parent(p, i) for i in range(N)]))
        
