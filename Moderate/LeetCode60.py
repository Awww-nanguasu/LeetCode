class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=[1]*n
        nums=list(map(str,range(1,n+1)))

        for i in range(1,n):
            fact[i]=fact[i-1]*i
        
        k-=1
        ans=[]

        for i in range(n):
            idx=k//fact[n-1-i]
            ans.append(nums.pop(idx))
            k%=fact[n-1-i]
        
        return "".join(ans)
