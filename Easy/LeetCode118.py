class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        Depth = 1
        queue = [[root]]
        
        while queue != [[]]:
            # print(queue)
            tmp = []
            for x in queue[0]:
                # print(queue[0])
                if x.left == None and x.right == None:
                    return Depth
                if x.left != None:
                    tmp.append(x.left)
                if x.right != None:
                    tmp.append(x.right)

            queue.append(tmp)
            queue.pop(0)
            Depth = Depth + 1
        return Depth
