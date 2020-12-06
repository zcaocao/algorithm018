'''
DP:
"(" + p + ")" + q  ==>  p + q = n - 1
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        if n == 0: return []
        total = []
        total.append([None]) # n = 0
        total.append(["()"]) # n = 1
        for i in range(2, n + 1):
            l = []
            for j in range(i):
                cur_l1 = total[j] # p
                cur_l2 = total[i - 1 - j] # q = (i-1)-j
                # enumerate cur_l1 and cur_l2
                for c1 in cur_l1:
                    for c2 in cur_l2:
                        if c1 == None:
                            c1 = ""
                        if c2 == None:
                            c2 = ""
                        el = "(" + c1 + ")" + c2
                        l.append(el)
            total.append(l)
        return total[n]
        '''
        dp  = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - 1 - j]]
        return dp[n]

