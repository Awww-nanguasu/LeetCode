class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1

            elif start != -1:
                j = start + 1
                match += 1
            else:
                return False
                
        return all(x == "*" for x in p[j:])

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        for j in range(1, n+1): 
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':  
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':            
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]  
        
        return dp[m][n]