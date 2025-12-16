
#Double pointer ⭐⭐⭐
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

# Cursion ⭐⭐

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        expectedNums = length
        total_iter = 0
        cur_pointer = 0
        while(total_iter<length-1):
            if nums[cur_pointer] == nums[cur_pointer+1]:
                del nums[cur_pointer]
                expectedNums -= 1
            else:
                cur_pointer = cur_pointer +1

            total_iter += 1
        return expectedNums