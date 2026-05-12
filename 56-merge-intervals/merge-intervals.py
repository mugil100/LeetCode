class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) #sort using the starting range
        op = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = op[-1][1]

            if start <=lastEnd:
                op[-1][1] = max(lastEnd,end)
            else:
                op.append([start,end])

        return op




        