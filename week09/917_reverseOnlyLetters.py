class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ls = list(S)
        l, r = 0, len(ls) - 1
        while l < r:
            while l < r and not ls[l].isalpha(): l += 1
            while l < r and not ls[r].isalpha(): r -= 1
            ls[l], ls[r] = ls[r], ls[l]
            l, r = l+1, r-1
        return ''.join(ls)
