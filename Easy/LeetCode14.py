
#horizon comparsion ⭐⭐
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        len_prefix = 0
        length, min_str_len = len(strs), len(strs[0])
        
        if length == 1:
            return strs[0]
        
        while(len_prefix < min_str_len):
            for i in range(length-1):
                if len_prefix == 0:
                    next_str_len = len(strs[i+1])
                    if min_str_len > next_str_len:
                        min_str_len = next_str_len

                    if min_str_len == 0:
                        return ''

                if strs[i][len_prefix] != strs[i+1][len_prefix]:
                    return prefix
                
            prefix += strs[i][len_prefix]
            len_prefix += 1
        return prefix
        
