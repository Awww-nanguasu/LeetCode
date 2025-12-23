
#隔板法 ⭐⭐⭐

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2) 

        if len1 == 0:
            return nums2
        if len2 == 0:
            return nums1
        
        if len1 == 1 and len2 == 1:
            return (nums1[0] + nums2[0])/2
        
        if len1 == 1:
            nums1 = [nums2[0], nums1[0], nums2[-1]]

        if len2 == 1:
            nums2 = [nums1[0], nums2[0], nums1[-1]]

        p1 = len1 // 2 - 1
        p2 = len2 // 2 - 1
        
        min_right = nums1[p1 + 1]
        min_flag = 0

        max_left = nums1[p1]
        max_flag = 0
        
        while(1):
            if nums2[p2] < nums1[p1]:
                max_left = nums1[p1]
                max_flag = 1
            else:
                max_left = nums2[p2]
                min_flag = 2    

            if nums2[p2 + 1] > nums1[p1 + 1]:
                min_right = nums1[p1 + 1]
                min_flag = 1
            else:
                min_right = nums2[p2 + 1]
                min_flag = 2

            len_left = p1 + p2 
            len_right = len1 + len2 - len_left

            if (len_left - len_right) >=2:
                if max_flag == 1:
                    p1 = p1 - 1
                    continue
                else:
                    p2 = p2 - 1
                    continue
        
            if (len_right - len_left) >=2:
                if min_flag == 1:
                    p1 = p1 + 1
                    continue
                else:
                    p2 = p2 + 1
                    continue

            if max_left > min_right:
                if max_flag == 1:
                    p1 = p1 - 1
                else:
                    p2 = p2 - 1

                if min_flag == 1:
                    p1 = p1 + 1
                else:
                    p2 = p2 + 1
            else:
                return (max_left + min_right)/2
        
        
        