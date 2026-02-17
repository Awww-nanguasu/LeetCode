# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [[root]]
        List = [[root.val]]
        while queue != [] and queue !=[[]]:
            tmp = []
            tmp_val = []
            for x in queue[0]:
                if x.left:
                    tmp.append(x.left)
                    tmp_val.append(x.left.val)

                if x.right:
                    tmp.append(x.right)
                    tmp_val.append(x.right.val)
            if tmp_val != []:
                List.append(tmp_val)    
            queue.append(tmp)
            
            queue.pop(0)
        return List