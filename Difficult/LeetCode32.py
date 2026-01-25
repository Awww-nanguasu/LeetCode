#failed
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        heap = ''
        length = len(s)
        max_str = 0
        cur_str = 0
        pre_con = 0
        flag = 0
        for i in range(length):
            if s[i] == '(' and i+1 == len(s):
                break
            
            if s[i] == '(' and s[i+1] == '(':
                pre_con = cur_str
                cur_str = 0
                heap = heap + s[i]
                flag = 1
                continue

            if s[i] == '(':
                heap = heap + s[i]

            if s[i] == ')' and len(heap)==0:
                cur_str = 0
                pre_con = 0
                heap = ''
                continue

            if s[i] == ')' and heap[-1] == '(':
                cur_str = cur_str + 1
                heap = heap[:-1]
            
            if len(heap) == 0 and flag == 1:
                cur_str = cur_str + pre_con
                pre_con = cur_str
                flag = 0
            
            if cur_str > max_str:
                max_str = cur_str

        return max_str*2
