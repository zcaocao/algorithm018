class Solution:
    '''
    中心扩散
    '''
    def isPalindroms(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = self.isPalindroms(s, i, i) # odd length
            l2, r2 = self.isPalindroms(s, i, i+1) # even length
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start: end+1]


