# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or inorder == []:
            return None

        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        
        cur_node = TreeNode(root_val)
        cur_node.left = self.buildTree(preorder[1:1+root_idx], inorder[:root_idx])
        cur_node.right = self.buildTree(preorder[1+root_idx:], inorder[1+root_idx:]) 
        return cur_node

