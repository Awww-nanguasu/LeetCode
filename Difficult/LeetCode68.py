class Solution(object):
    def fullJustify(self, words, maxWidth):
        def getEl(start, end, cnt):
            row = ""
            if end == n - 1:
                for i in range(start, end):
                    row += words[i] + " "
                row += words[end]
                while len(row) < maxWidth:
                    row += " "
            else:
                num = end - start + 1  
                space = maxWidth - cnt + num - 1 
                i = start
                while space > 0:
                    words[i] += " "
                    space -= 1
                    i += 1
                    if i >= end:
                        i = start
                for i in range(start, end + 1):
                    row += words[i]
            return row

        n = len(words)
        i = 0
        res = []
        while i < n:
            start = i
            cnt = len(words[i])
            while i + 1 < n and cnt + len(words[i + 1]) + 1 <= maxWidth:
                i += 1
                cnt += len(words[i]) + 1
            res.append(getEl(start, i, cnt))
            i += 1
        return res

