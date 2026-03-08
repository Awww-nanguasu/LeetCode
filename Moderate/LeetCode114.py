# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        isLeft = self.flatten(root.left)
        isRight = self.flatten(root.right)

        if isLeft:
            tmp = root.right
            root.right = root.left
            root.right.right = tmp

class Solution:
    # 定义：将以 root 为根的树拉平为链表
    def flatten(self, root) -> None:
        # base case
        if root is None:
            return

        # 利用定义，把左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 2、将左子树作为右子树
        root.left = None
        root.right = left

        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right