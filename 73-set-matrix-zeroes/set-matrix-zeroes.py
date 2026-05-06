class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_len = len(matrix)
        col_len = len(matrix[0])
        row= set()
        col = set()
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        for r in row:
            for i in range(col_len):
                matrix[r][i]=0  #set cols to 0
        for c in col:
            for i in range(row_len):
                matrix[i][c]=0  #set rows to 0
                  

                
        