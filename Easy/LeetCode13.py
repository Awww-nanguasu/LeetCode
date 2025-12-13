#hashmap ⭐⭐
class Solution:
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def romanToInt(self, s: str) -> int:
        n = len(s)
        dict = self.dict
        output = dict[s[-1]]
        for i in range(n-1):
            if dict[s[i]]<dict[s[i+1]]:
                output -= dict[s[i]]
            else:
                output += dict[s[i]]
        return output