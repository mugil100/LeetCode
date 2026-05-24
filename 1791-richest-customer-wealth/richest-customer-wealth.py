class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        collen = len(accounts[0])
        rowlen = len(accounts)
        richest = 0
        for i in range(rowlen):
            temp=0
            for j in range(collen):
                temp+=accounts[i][j]
            if temp > richest:
                richest = temp
        return richest
        