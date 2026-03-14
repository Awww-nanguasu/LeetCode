# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or postorder == []:
            return None
        root_val = preorder[0]
        root_idx = postorder.index(root_val)
        cur_node = TreeNode(root_val)

        cur_node.left = self.constructFromPrePost(preorder[1:1+root_idx], postorder[:root_idx])
        cur_node.right = self.constructFromPrePost(preorder[1+root_idx:], postorder[root_idx+1:])
    
        return cur_node