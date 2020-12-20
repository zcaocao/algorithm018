class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Space: O(n)
        isPalindrom = lambda x: x == x[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:  # 判断去掉一个字母，中间未比较部分是否构成回文
                   #                 (left, right]                   [left, right)
                return isPalindrom(s[left+1:right+1]) or isPalindrom(s[left:right])
        return True
