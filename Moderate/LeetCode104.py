# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [[root]]
        List = [[root.val]]
        while queue != []:
            tmp = []
            for x in queue[0]:
                if root.left:
                    tmp.append(root.left)
                    List.append(root.left)

                if root.right:
                    tmp.append(root.right)
                    List.append(root.right)
                
                queue.append(tmp)
                queue.pop(0)
        return List