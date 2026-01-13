class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea

        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = (j-i)*min(height[i],height[j])
        while i < j and i+1 <= len(height)-1 and j-1>=0:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            ans = max(ans, (j-i)*min(height[i],height[j]))
        return ans
        