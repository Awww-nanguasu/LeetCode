# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct(root, path):
            if root:
                path += str(root.val)    
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path = path + '->'
                    construct(root.left, path)
                    construct(root.right, path)

        paths = []
        construct(root, '')
        return paths