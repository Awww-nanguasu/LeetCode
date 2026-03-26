# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        queue = [[root]]

        flag = 0
        while not all(x is None for x in queue[0]):
            tmp = []
            count = 0
            for x in queue[0]:
                if x == None:
                    flag = 1
                else:
                    if flag == 1:
                        return False
                    tmp.append(x.left)
                    tmp.append(x.right)    
                
            queue.append(tmp)
            queue.pop(0)
        return True