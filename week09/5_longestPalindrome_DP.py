class Solution:
    '''
    DP: 
    '''
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举字符串长度 (l+1)
        for l in range(n):
            # 枚举起始位置i，结束位置即i+l
            for i in range(n):
                j = i+l
                if j >= n:
                    break
                if l == 0: # 只有一个字母，是回文
                    dp[i][j] = True
                elif l == 1: # 只有两个字母
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans
