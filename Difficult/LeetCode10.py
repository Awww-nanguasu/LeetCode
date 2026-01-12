class Solution:
    def isMatch(self, s: str, p: str, flag=1) -> bool:
        if len(p) == 0 and len(s) == 0:
            return True

        if len(p) == 0 and len(s) !=0:
            return False

        if len(s) == 0 and len(p) !=0:
            return False


        if flag:
            s = s[::-1]
            p = p[::-1]

        if p[0] == '*' and len(p) == 1:
            return False
        
        if p[0] == '*' and p[1] == '.':
            p = p[2:] + p[0]
            return self.isMatch(s, p, 0)

        if p[0] == '*':
            for j in range(1, len(p)):
                if p[j] != s[0]:
                    break
            p = p[j:]

            for i in range(len(s)):
                if s[i] != s[0]:
                    break
            s = s[i:]

            if p[0] == '.':
                return self.isMatch(s, p, 0) or self.isMatch(s, p[1:], 0)
        
        if p[0] == '.' or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:], 0)
