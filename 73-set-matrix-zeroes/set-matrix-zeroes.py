class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        n_col = len(matrix[0])
        res=[]
        for i in range(n):
            for j in range(n_col):
                if matrix[i][j]==0:
                    res.append([i,j])
        for (i,j) in res:
            for a in range(n):
                matrix[a][j]=0
            for b in range(n_col):
                matrix[i][b]=0
        del res
            

                
        