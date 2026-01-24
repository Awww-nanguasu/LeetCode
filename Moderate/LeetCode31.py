class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
#failed
def nextPermutation(nums) -> None:
    flag = 0
    print(-len(nums)+1)
    for i in range(-1,-len(nums),-1):
        if nums[i] > nums[i-1]:
            flag = 1
            tmp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = tmp  
            break
                      
    if flag == 0:
        nums[:] = nums[::-1]
    
nums = [1,3,2]
nextPermutation(nums)
print(nums)