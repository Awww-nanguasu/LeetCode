"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.List = []
        self.queue = []

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return root
            
        self.queue.append([root])

        while self.queue != [[]] and self.queue!=[]:
            tmp_val = []
            tmp = []
            
            for x in self.queue[0]:
                tmp_val.append(x.val)
                tmp = tmp + x.children
            
            self.queue.append(tmp)
            self.List.append(tmp_val)

            self.queue.pop(0)
        
        return self.List