class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)

        i = 0
        if s[i] in "+-":
            i += 1

        has_dot = has_digit = False
        while i < n and s[i] not in "eE":
            if s[i] == '.':
                if has_dot: 
                    return False
                has_dot = True
            elif '0' <= s[i] <= '9':
                has_digit = True
            else:
                return False
            i += 1

        if not has_digit:
            return False

        if i < n and s[i] in "eE":
            i += 1

            if i < n and s[i] in "+-":
                i += 1

            if i == n:
                return False

            while i < n and '0' <= s[i] <= '9':
                i += 1

        return i == n
