class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        mod_index = defaultdict(int) 
        mod_index[0] = -1 

        for i, num in enumerate(nums):
            total += num
            mod = total % k

            if mod in mod_index:
                if i - mod_index[mod] > 1:
                    print("mod", mod, mod_index)
                    return True
            else:
                mod_index[mod] = i

        return False
