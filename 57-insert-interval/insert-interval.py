class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        op = [intervals[0]]

        for start, end in intervals:
            lastEnd = op[-1][1]
            if start <=lastEnd:
                op[-1][1] = max(lastEnd, end)
            else:
                op.append([start,end])
        return op

        