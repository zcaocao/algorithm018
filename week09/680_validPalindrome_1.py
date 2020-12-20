class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Space: O(1)
        def isPalindrom(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:  # 判断去掉一个字母，中间未比较部分是否构成回文
                   #               (left, right]                [left, right)
                return isPalindrom(left+1, right) or isPalindrom(left, right-1)
        return True
