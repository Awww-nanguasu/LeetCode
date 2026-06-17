class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 买入再卖出算一次交易
        @cache
        def dfs(i,hold,r):
            if i==len(prices):
                return 0 if not hold and r<=2 else -inf
            if hold:
                return max(dfs(i+1,hold,r),prices[i]+dfs(i+1,0,r))
            else:
                return max(dfs(i+1,hold,r),-prices[i]+dfs(i,1,r))
        ans=dfs(0,0,0)
        dfs.cache_clear()
        return ans
