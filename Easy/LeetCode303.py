class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumArray = self.sumPre()

    def sumPre(self):
        sumArray = [0] * len(self.nums)
        for i in range(len(self.nums)):
            if i == 0:
                sumArray[i] = self.nums[i]
            else:
                sumArray[i] = sumArray[i-1] + self.nums[i]
        print(sumArray)
        return sumArray

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumArray[right] - 0
        return self.sumArray[right] - self.sumArray[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)