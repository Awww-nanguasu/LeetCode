class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(l, r):
            if l > r:
                return [None]
            ans = []
            for i in range(l, r + 1):
                for x in dfs(l, i - 1):
                    for y in dfs(i + 1, r):
                        root = TreeNode(i)
                        root.left, root.right = x, y
                        ans.append(root)
            return ans
        return dfs(1, n)
