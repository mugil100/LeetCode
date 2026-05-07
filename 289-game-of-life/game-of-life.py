class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        nbc=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                ind = (i,j) 
                neighbours = 0
                for r,c in offsets:
                    if 0<=i+r<=rows-1 and 0<=j+c<=cols-1 and board[i+r][j+c]==1:
                        neighbours+=1
                nbc.append(neighbours)
        ind=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if nbc[ind]<2:
                    board[i][j]=0
                if nbc[ind]<=3:
                    pass
                if nbc[ind]>3:
                    board[i][j]=0
                if nbc[ind]==3:
                    board[i][j]=1
                ind+=1
