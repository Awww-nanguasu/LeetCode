class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = slow = 0
        while(fast<len(nums)):
            nums[slow] = nums[fast]
            if nums[fast] != 0:
                slow = slow + 1
            fast = fast + 1
        
        nums[slow:] = [0]*(fast-slow)
        return nums