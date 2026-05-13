class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        n = len(points)
        res = 1
        prev = points[0]

        for i in range(1,n):
            start,end = points[i]
            if start <= prev[1]:
                prev = [start, min(end,prev[1])]
            else:
                prev = [start,end]
                res+=1
        return res


        