class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key = lambda x: x[1])
    #     res = [intervals[0]]

    #     for idx in range(1, len(intervals)):
    #         if res[-1][1] <= intervals[idx][0]:
    #             res.append(intervals[idx])
        
    #     return len(intervals) - len(res)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        maxEndPoint = intervals[0][1]
        count = 0

        for idx in range(1, len(intervals)):
            if intervals[idx][0] < maxEndPoint:
                count += 1
            else:
                maxEndPoint = max(maxEndPoint, intervals[idx][1])
        
        return count