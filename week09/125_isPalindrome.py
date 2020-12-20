class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 双指针
        tmp = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(tmp)-1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        return True

        '''
        # python comprehensive.
        res = "".join(ch.lower() for ch in s if ch.isalnum())
        return res == res[::-1]
        '''
        '''
        isalnum(): 检测字符串是否由字母和数字组成。
        '''
