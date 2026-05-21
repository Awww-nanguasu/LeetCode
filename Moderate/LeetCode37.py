class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set = [set() for _ in range(9)] 
        col_set = [set() for _ in range(9)] 
        sub_box_set = [[set() for _ in range(3)] for _ in range(3)] 
        empty_pos = [] 
        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    empty_pos.append((i, j))
                else:
                    x = int(b)

                    row_set[i].add(x)
                    col_set[j].add(x)
                    sub_box_set[i // 3][j // 3].add(x)

        get_candidates = lambda i, j: 9 - len(row_set[i] | col_set[j] | sub_box_set[i // 3][j // 3])
        empty_heap = [(get_candidates(i, j), i, j) for i, j in empty_pos]
        heapify(empty_heap)

        def dfs() -> bool:
            if not empty_heap:
                return True  

            _, i, j = heappop(empty_heap)

            candidates = 0 
            for x in range(10):
                if x in row_set[i] or x in col_set[j] or x in sub_box_set[i // 3][j // 3]:
                    continue 

                board[i][j] = digits[x]
                row_set[i].add(x)
                col_set[j].add(x)
                sub_box_set[i // 3][j // 3].add(x)

                if dfs():
                    return True

                row_set[i].remove(x)
                col_set[j].remove(x)
                sub_box_set[i // 3][j // 3].remove(x)

                candidates += 1

            heappush(empty_heap, (candidates, i, j))

        dfs()

