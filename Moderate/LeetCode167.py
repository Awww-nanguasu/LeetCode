class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        idx1, idx2 = 0, n-1
        while idx1 < idx2:
            sum1 = numbers[idx1] + numbers[idx2] 
            if  sum1 == target:
                return [idx1 + 1, idx2 + 1]
            elif sum1 < target:
                idx1 += 1
            else:
                idx2 -= 1
