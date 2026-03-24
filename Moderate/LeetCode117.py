"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        queue = [[root]]
        while queue!=[[]]:
            tmp = []
            Dummy = Node()
            pre = Dummy
            for x in queue[0]:
                pre.next = x
                if x.left:
                    tmp.append(x.left)
                
                if x.right:
                    tmp.append(x.right)
                pre = x
                pre.next = None
            queue.append(tmp)
            queue.pop(0)
        return root
