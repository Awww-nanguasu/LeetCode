#cursion ⭐⭐⭐

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in range(-1, -len(s)-1, -1):
            if s[i]!=' ':
                length += 1

            if s[i] == ' ' and length!=0:
                return length

            if length == len(s):
                return length
            
        return length