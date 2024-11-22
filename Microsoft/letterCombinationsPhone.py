class Solution:
    def letterCombinations(self, digits):
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backTrack(index, letters):
            if index == len(digits):
                result.append(letters)
                return

            for letter in digitToChar[digits[index]]:
                backTrack(1+index, letter+letters)

        if not digits:
            return result

        backTrack(0, "")
        return result


print(Solution().letterCombinations("23"))
