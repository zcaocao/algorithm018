class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        # dp[i]表示以s[i-1]结尾的前缀解码数，dp[n]表示s[n-1]，s下标是0到n-1
        dp = [0 for _ in range(n + 1)] 
        dp[0] = 1
        dp[1] = 1 if int(s[0]) != 0 else 0
        for i in range(1, n): 
            # 第i-1 和 i 位构成10 ～ 26以内数字
            '''
            if int(s[i-1]) == 1 or int(s[i-1]) == 2 and int(s[i]) < 7:
                if int(s[i]) == 0: dp[i+1] = dp[i-1] # 10 或 20
                else: dp[i+1] = dp[i] + dp[i-1]
            elif int(s[i]) == 0: return 0
            else: dp[i+1] = dp[i]
            '''
            if int(s[i]) != 0: dp[i+1] = dp [i]
            if int(s[i-1]) == 1 or int(s[i-1]) == 2 and int(s[i]) < 7: dp[i+1] += dp[i-1]
            
        return dp[n] 

