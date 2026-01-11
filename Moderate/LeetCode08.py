
# interation 2 star
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        flag = 0
        for i in range(len(s)):
            if flag==0 and s[i]==' ':
                continue

            if flag==0 and s[i]=='-':
                flag = 1
                continue

            if flag==0 and s[i]=='+':
                flag = 2
                continue

            if ord(s[i])<48 or ord(s[i])>57:
                break

            if (res>(2**31 -1)//10) or (res==(2**31 -1)//10 and int(s[i])>7):
                if flag == 2 or flag == 0:
                    return 2**31 - 1
                else:
                    return -2**31

            res = res*10 + int(s[i])

            if flag==0:
                flag = 2
            
        if flag == 2 or flag == 0:
            return res
        else:
            return -res
            