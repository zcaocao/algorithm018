class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(index: int):
            # terminator
            if index == len(digits):
                combinations.append("".join(combination))
            else: # process current level
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    # drill down
                    backtrack(index + 1)
                    # reverse current level status
                    combination.pop()
        
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
