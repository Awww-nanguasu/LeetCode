class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0]*n
        for i in range(len(bookings)):
            tmp = bookings[i][2]
            nums[bookings[i][0]-1] += tmp
            if bookings[i][1] < n:
                nums[bookings[i][1]] -= tmp
        for j in range(1, len(nums)):
            nums[j] = nums[j] + nums[j-1]
        
        return nums