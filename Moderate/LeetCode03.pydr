# slide Winodw ⭐⭐
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = ''
        max_len = 0

        for x in s:
            if x in window:
                idx = window.index(x)
                window = window[idx+1:]
            
            window += x
            if len(window) > max_len:
                max_len = len(window)

        return max_len