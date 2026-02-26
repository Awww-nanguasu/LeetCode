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
    
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for node, index in arr:
                if node.left:
                    tmp.append([node.left, index * 2])
                if node.right:
                    tmp.append([node.right, index * 2 + 1])
            res = max(res, arr[-1][1] - arr[0][1] + 1)
            arr = tmp
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans, queue = 0, deque([(1, root)])
        while queue:
            mn, mx = inf, 0
            for _ in range(len(queue)):
                code, node = queue.popleft()
                if node.left:
                    queue.append((code * 2, node.left))
                if node.right:
                    queue.append((code * 2 + 1, node.right))
                mn, mx = min(code, mn), max(code, mx)
            ans = max(ans, mx - mn + 1)
        return ans

