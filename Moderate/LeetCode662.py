# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        queue = [[root]]
        max_depth = 1

        while queue != [[]]:
            tmp = []
            flag = 0
            for x in queue[0]:
                if x.left:
                    tmp.append(x.left)
                    if x.right == None:
                        flag += 1

                if x.right:
                    tmp.append(x.right)
                    if x.left == None:
                        flag += 1
            
            if len(tmp)+flag > max_depth:
                max_depth = len(tmp)+flag

            queue.append(tmp)
            queue.pop(0)
        
        return max_depth