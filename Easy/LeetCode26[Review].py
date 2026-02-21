class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        slow = 1
        fast = 1

        while(fast<n):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow = slow + 1

            fast = fast + 1
        
        return slow