#failed

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deque = collections.deque([root])
        max_final = 1
        res = 0
        
        while deque:
            tmp = []
            res = 0
            cur_final = 0

            for _ in range(len(deque)):
                node = deque.popleft()
                
                if node.left or len(tmp)!=0:
                    if node.left == None:
                        res = res + 1
                    else:
                        tmp.append(node.left)
                        cur_final = len(tmp) + res

                if node.right or len(tmp)!=0:
                    if node.right == None:
                        res = res + 1
                    else:
                        tmp.append(node.right)
                        cur_final = len(tmp) + res

                print("res", res)
                print("tmp", tmp, len(tmp))
                print(node)
                print("+++++++++++++++")

            if cur_final > max_final:
                max_final = cur_final

            if tmp != []:
                deque = deque+ collections.deque(tmp)
        return max_final