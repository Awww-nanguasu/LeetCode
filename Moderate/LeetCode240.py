class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        up = 0
        down = m - 1
        while up <= down:
            mid = up + (down - up) // 2
            if matrix[mid][0] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            elif matrix[mid][0] == target:
                return True
        
        for row in range(up):
            nums = matrix[row]
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    return True
        
        return False