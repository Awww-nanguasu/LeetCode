

#逐位判断 ⭐
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
            
        if x<10:
            return True

        n = int(log10(x)) + 1
        if n == 1:
            if x%10 != x//10:
                return False
            return True

        half_n = n//2

        for i in range(half_n):
            a = x//10**(n - 1 - i) 
            b = x%10**(i + 1) 

            if i!=0:
                a = a % 10
                b = b // 10**i

            if a != b:
                return False
        return True 