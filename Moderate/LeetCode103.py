# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = [[root]]
        List = [[root.val]]
        i = 1
        while queue != [[]]:
            tmp = []
            tmp_val = []

            for x in queue[0]:
                
                if x.left:
                    tmp_val.append(x.left.val)
                    tmp.append(x.left)
                
                if x.right:
                    tmp_val.append(x.right.val)
                    tmp.append(x.right)
            
            if i % 2!=0:
                tmp_val.reverse()
            
            i = i + 1
            queue.append(tmp)
            queue.pop(0)

            if tmp_val:
                List.append(tmp_val)
        
        return List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res = []
        deque = collections.deque([root])

        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) %2 == 0:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
            
                if node.left:
                    deque.append(node.left)
            
                if node.right:
                    deque.append(node.right)
            
            res.append(list(tmp))
        
        return res
