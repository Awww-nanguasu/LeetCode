class Solution(object):
    def recoverTree(self, root):
        nodes = []
 
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        x = None
        y = None
        pre = nodes[0]

        for i in range(1,len(nodes)):
            if pre.val>nodes[i].val:
                y=nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]

        if x and y:
            x.val,y.val = y.val,x.val

