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

    def postorder(self, root: 'Node') -> List[int]:
        if root != None:
            for x in root.children:
                self.postorder(x)
            
            self.List.append(root.val)
        return self.List
    
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node: 'Node'):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans
