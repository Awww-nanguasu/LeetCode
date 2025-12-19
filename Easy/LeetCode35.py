# 二分法 ⭐⭐

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start_pointer = -1
        end_pointer = length

        while(start_pointer + 1 < end_pointer):
            base_pointer = (end_pointer + start_pointer)// 2
            if target == nums[base_pointer]:
                return base_pointer
            elif target < nums[base_pointer]:
                end_pointer = base_pointer
            else:
                start_pointer = base_pointer
        
        return end_pointer