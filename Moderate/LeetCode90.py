class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res
        
    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for mask in range(1 << n):
            t = []
            flag = True
            for i in range(n):
                if mask & (1 << i):
                    if i > 0 and not (mask & (1 << (i - 1))) and nums[i] == nums[i - 1]:
                        flag = False
                        break
                    t.append(nums[i])
            if flag:
                ans.append(t)
        return ans
