# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_nums = 0

    def cumsum(self, root, cur_nums):
        if root:
            cur_nums = cur_nums*10
            cur_nums += root.val
            if not root.left and not root.right:
                self.total_nums += cur_nums
            else:
                
                self.cumsum(root.left, cur_nums)
                self.cumsum(root.right, cur_nums)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_nums = 0
        cur_nums = 0
        self.cumsum(root, cur_nums)
        return self.total_nums