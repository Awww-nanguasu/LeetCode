#failed
class Solution:
    def bisect(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left<=right):
            middle = (left + right) // 2
            if nums[middle] == target:
               break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return middle

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0]>target:
            return [-1, -1]

        a = self.bisect(nums, target+1)
        b = self.bisect(nums, target-1)
        if a == b or (nums[a-1] == target-1) or (nums[b+1] == target+1):
            return [-1, -1]
        else:
            return [b+1, a-1]