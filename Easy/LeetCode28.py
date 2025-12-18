class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        prefix_len = 0
        next = [0]
        j = 1
        while(j < needle_length):
            if needle[prefix_len] == needle[j]:
                prefix_len += 1
                next.append(prefix_len)
                j += 1
            else:
                if prefix_len == 0:
                    next.append(prefix_len)
                    j += 1
                else:
                    prefix_len = next[prefix_len - 1]

        i = 0
        k = 0
        haystack_len = len(haystack)

        if haystack_len < needle_length:
            return -1

        fit_num = 0
        while(i < haystack_len):
            if haystack[i] == needle[k]:
                i += 1
                k += 1
            else:
                if k == 0:
                    i += 1
                    k = 0
                else:  
                    k = next[k - 1]

            if k == needle_length:
                return i - needle_length
        return -1