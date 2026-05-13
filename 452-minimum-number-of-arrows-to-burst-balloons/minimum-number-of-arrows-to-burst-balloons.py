class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        n = len(points)
        res = 1
        curr_end = points[0][1]

        for i in range(1,n):
            if points[i][0] > curr_end:
                res+=1
                curr_end = points[i][1]
        return res


        