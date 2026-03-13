# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == [] or postorder == []:
            return None
        
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        cur_node = TreeNode(root_val)
        cur_node.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        cur_node.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        return cur_node