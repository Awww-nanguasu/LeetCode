class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pre = self.preGreaterElement(nums2)
        greater_map = {}
        for i in range(len(nums2)):
            greater_map[nums2[i]] = pre[i]
        res = [greater_map[num] for num in nums1]
        return res


    def preGreaterElement(self, nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = [-1]*n
        s = []
        for idx in range(n-1, -1, -1):
            while s and s[-1] < nums2[idx]:
                s.pop()
            
            res[idx] = -1 if not s else s[-1]
            s.append(nums2[idx])
        return res 