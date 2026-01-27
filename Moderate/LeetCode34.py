class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 左闭右开区间 [left, right)
        while left < right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid  # 范围缩小到 [left, mid)
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right)
        # 循环结束后 left = right
        # 此时 nums[left-1] < target 而 nums[left] = nums[right] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]


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