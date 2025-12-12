# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。

#hashtable ⭐⭐
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hastable = dict()
        for i, num in enumerate(nums):
            if target - num in hastable:
                return [hastable[target - num], i]
            hastable[nums[i]] = i
        return []


# numpy 解法 ❌ 内存超标

import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = np.array(nums)
        tmp = nums.reshape(-1, 1) + nums
        row, col = np.where(tmp == target)

        final_indices = []

        for r, c in zip(row, col):
            if r != c:
                final_indices = [int(r), int(c)]
                break
        return final_indices