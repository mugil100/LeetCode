class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        res = n

        if n ==1:
            return 1

        prev = points[0]

        for i in range(1,n):
            start,end = points[i]
            if start <= prev[1]:
                res-=1
                prev = [start, min(end,prev[1])]
            else:
                prev = [start,end]
        return res


        