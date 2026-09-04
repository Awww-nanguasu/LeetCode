class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            tmp = 0
            p0, p1 = i + 1, n - 1
            while p0 < p1:
                if i>0 and nums[i] == nums[i-1]:
                        continue
                tmp = nums[i] + nums[p0] + nums[p1]
                if tmp > 0:
                    p1 -= 1
                    while nums[p1] == nums[p1+1] and p1>0:
                        p1 -= 1
                elif tmp < 0:
                    p0 += 1
                    while nums[p0] == nums[p0-1] and p0<p1:
                        p0 += 1
                else:
                    res.append([nums[i], nums[p0], nums[p1]])
                    p0 += 1
                    while nums[p0] == nums[p0-1] and p0<p1:
                        p0 += 1
        return res