# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.List = []
    def travel(self, node):
        if node != None:
            self.travel(node.left)
            self.List = self.List + [node.val]
            self.travel(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.travel(root)
        return self.List