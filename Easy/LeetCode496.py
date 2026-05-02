class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.nextGreaterElementInternal(nums2)
        greater_map = {}
        for i in range(len(nums2)):
            greater_map[nums2[i]] = greater[i]
        res = [greater_map[num] for num in nums1]
        return res

    def nextGreaterElementInternal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return res