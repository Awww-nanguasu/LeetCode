# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums = nums.sort()

#         if len(nums)<4:
#             return list()

#         left1 = 0
#         left2 = 1
#         left3 = 2
#         left4 = 3

#         for i in range(n-4):
#             for j in range(i+1, n-3):
#                 fourth = n - 1
#                 third = j + 1

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         quadruplets = list()
#         if not nums or len(nums) < 4:
#             return quadruplets
        
#         nums.sort()
#         length = len(nums)
#         for i in range(length - 3):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
#                 break
#             if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
#                 continue
#             for j in range(i + 1, length - 2):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
#                     break
#                 if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
#                     continue
#                 left, right = j + 1, length - 1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right]
#                     if total == target:
#                         quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         left += 1
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
#                         right -= 1
#                     elif total < target:
#                         left += 1
#                     else:
#                         right -= 1
        
#         return quadruplets
# #failed
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()

#         if n<4:
#             return list()

#         if n == 4:
#             if sum(nums) == target:
#                 return [nums]
#             else:
#                 return list() 

#         result = []

#         for i in range(n-4):
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, n-3):
#                 if j>i+1 and nums[j] == nums[j-1]:
#                     continue
#                 fourth = n - 1
#                 third = j + 1

#                 while(third < fourth):
#                     if third > j+1 and nums[third] == nums[third-1]:
#                         third = third + 1
#                         continue

#                     if fourth < n-1 and nums[fourth] == nums[fourth+1]:
#                         fourth = fourth - 1
#                         continue

#                     four_sum = nums[i] + nums[j] + nums[third] + nums[fourth]
#                     if four_sum > target:
#                         fourth = fourth - 1
#                         continue
                    
#                     if four_sum < target:
#                         third = third + 1
#                         continue

#                     if four_sum == target:
#                         result.append([nums[i], nums[j], nums[third], nums[fourth]])
#                         third = third + 1
#                         continue
#         return result

def fourSum(nums, target: int):
    n = len(nums)
    nums.sort()

    if n<4:
        return list()
                
    result = []

    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j>i+1 and nums[j] == nums[j-1]:
                    continue
            fourth = n - 1
            third = j + 1

            while(third < fourth):
                if third > j+1 and nums[third] == nums[third-1]:
                    third = third + 1
                    continue

                if fourth < n-1 and nums[fourth] == nums[fourth+1]:
                    fourth = fourth - 1
                    continue

                four_sum = nums[i] + nums[j] + nums[third] + nums[fourth]
                if four_sum > target:
                    fourth = fourth - 1
                    continue
                    
                if four_sum < target:
                    third = third + 1
                    continue

                if four_sum == target:
                    result.append([nums[i], nums[j], nums[third], nums[fourth]])
                    third = third + 1
                    continue
    return result

fourSum([-1,0,1,2,-1,-4], -1)