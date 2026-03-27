# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent_tree = []

    def target_find(self, root: TreeNode, target: TreeNode) -> TreeNode:
        if root is None:
            return None

        if root == target:
            return root

        left_tree = self.target_find(root.left, target)
        if left_tree:
            self.parent_tree.append(left_tree)
            return root
        
        right_tree = self.target_find(root.right, target)
        if right_tree:
            self.parent_tree.append(right_tree)
            return root
        
        return None
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent_tree.append(self.target_find(root, target))
        
        queue = [[self.parent_tree[0]]]
        hashmap = [self.parent_tree[0]]
        tmp = hashmap
        count = 0
        while queue!=[[]] and count<k:
            tmp = []
            # print("enter", [x.val for x in queue[0]])
            # print("hash map", [x.val for x in hashmap])
            for x in queue[0]:
                if x.left and x.left not in hashmap:
                    hashmap.append(x.left)
                    tmp.append(x.left)
                
                if x.right and x.right not in hashmap:
                    hashmap.append(x.right)
                    tmp.append(x.right)
            # print("out", [x.val for x in tmp])
            count += 1
            queue.pop(0)
            if count<len(self.parent_tree):
                tmp.append(self.parent_tree[count])
                hashmap.append(self.parent_tree[count])
            queue.append(tmp)
    
            # print("count", count)
            # print("parent_tree", [x.val for x in self.parent_tree])
            # print("queue", [x.val for x in queue[0]])
        return [x.val for x in tmp]
        