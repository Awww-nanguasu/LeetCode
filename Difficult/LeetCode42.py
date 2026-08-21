class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack = []

        for idx, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = idx - left - 1
                currHeight = min(h, height[left]) - height[top]
                ans += currHeight*currWidth 
            stack.append(idx)
        return ans


