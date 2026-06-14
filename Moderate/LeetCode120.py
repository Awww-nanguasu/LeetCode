class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        li = triangle[-1]

        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                li[j] = min(li[j] , li[j]) + triangle[i][j]
        
        return li[0]
