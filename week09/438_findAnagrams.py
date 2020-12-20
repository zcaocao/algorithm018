class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, len_s, len_p = [], len(s), len(p)
        if len_p > len_s: return res
        compare, temp = [0]*26, [0]*26
        # 统计p中字母出现次数，及s串中首个p窗口长度的字串中字母出现次数
        for i in range(len_p):
            compare[ord(p[i]) - ord('a')] += 1
            temp[ord(s[i]) - ord('a')] += 1
        # 滑动窗口遍历s串
        for i in range(0, len_s - len_p + 1):
            if compare == temp:
                res.append(i)
            # 窗口右移，弹出左边界，新的有边界进入temp统计
            if i+len_p < len_s:
                temp[ord(s[i]) - ord('a')] -= 1
                temp[ord(s[i+len_p]) - ord('a')] += 1
        return res
        
