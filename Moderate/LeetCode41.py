class Solution(object):
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            if nums[i]-1 >= 0 and nums[i]-1 <len(nums) and nums[i] != i+1:
                temp = nums[nums[i]-1]
                if temp != nums[i]:
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
                    continue
            i+=1
                
        
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                break
            i+=1
        return i+1
                    
