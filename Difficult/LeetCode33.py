class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        end = len(nums) - 1
        right = end

        if target <= nums[end]:
            flag = 1
        else:
            flag = 0

        while(left<=right):
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                if nums[middle] <= nums[end]:
                    right = middle - 1
                else:
                    if flag == 1:
                        left = middle + 1
                    else:
                        right = middle - 1
            else:
                if flag == 1:
                    left = middle + 1
                else:
                    if nums[middle] <= nums[end]:
                        right = middle - 1
                    else:  
                        left = middle + 1
        return -1