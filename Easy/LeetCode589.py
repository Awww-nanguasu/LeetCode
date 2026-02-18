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

    def travel(self, root):
        if root != None:
            self.List.append(root.val)
            for x in root.children:
                self.travel(x)

    def preorder(self, root: 'Node') -> List[int]:
        self.travel(root)
        return self.List