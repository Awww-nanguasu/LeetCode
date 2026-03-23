# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = [[root]]
        result = []
        while queue!= [[]]:
            tmp = []
            length = len(queue[0])
            result.append(queue[0][length-1].val)
            for x in queue[0]:
                if x.left:
                    tmp.append(x.left)
                
                if x.right:
                    tmp.append(x.right)

            queue.pop(0)
            queue.append(tmp)
        
        return result