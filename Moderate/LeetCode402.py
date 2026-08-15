class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        queue = []
        idx = 0

        for i in range(len(num)):
            while queue and int(queue[-1]) > int(num[i]) and idx < k:
                queue.pop()
                idx += 1

            queue.append(num[i])
        
        while queue and queue[0] == '0':
            queue.pop(0)

        

        if idx == k:
            result = ''.join(queue)
        else:
            result = ''.join(queue[:idx - k])
        
        return result if result else '0'