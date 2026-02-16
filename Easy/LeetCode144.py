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
        if node == None:
            return []
        self.List = self.List + [node.val]
        self.travel(node.left)
        self.travel(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.travel(root)
        return self.List