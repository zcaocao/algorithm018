#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        dict = collections.defaultdict(int)
        for i in range(len(s)):
            dict[s[i]] += 1
            dict[t[i]] -= 1

        for val in dict.values():
            if val:
                return False

        return True  
