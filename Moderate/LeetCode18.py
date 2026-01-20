class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = nums.sort()

        if len(nums)<4:
            return list()

        left1 = 0
        left2 = 1
        left3 = 2
        left4 = 3

        for i in range(n-4):
            for j in range(i+1, n-3):
                fourth = n - 1
                third = j + 1