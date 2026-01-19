class Solution:
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

    def letterCombinations(self, digits: str) -> List[str]:
        if str == '':
            return ''

        tmp = phoneMap[digits[0]]
        for i in len(tmp):
            list.append(tmp[i] + self.letterCombinations(digits[1:]))

        return list 
