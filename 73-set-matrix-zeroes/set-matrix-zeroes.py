class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_len = len(matrix)
        col_len = len(matrix[0])
        row0 = False
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        row0 = True

        for r in range(1,row_len):
            for c in range(1,col_len):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(row_len):
                matrix[r][0]=0

        if row0:
            for c in range(col_len):
                matrix[0][c]=0        

                


                
                    
        
                  

                
        