class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        All_sum = sum(nums)
        n = len(nums) + 1
        PreSum = [0]*n
        for i in range(1, n):

            PreSum[i] = PreSum[i-1] + nums[i-1]
            if All_sum - PreSum[i] == PreSum[i-1]:
                return i-1
        return -1