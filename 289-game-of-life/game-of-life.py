class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def neighbour(r,c):
            n=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if( i<0 or i==rows or j<0 or j==cols or (i==r and j==c)):
                        continue
                    else:
                        if board[i][j] in [1,3]:
                            n+=1
            return n

        for r in range(rows):
            for c in range(cols):
                nbrs = neighbour(r,c)
                if board[r][c]:
                    if nbrs in [2,3]:
                        board[r][c]=3 #1->1     #if nbrs<2: 1->0
                else:
                    if nbrs==3:
                        board[r][c]=2 #0->1     #if nbrs<3: 0->0 
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==1:
                    board[r][c]=0
                elif board[r][c] in [2,3]:
                    board[r][c]=1


        