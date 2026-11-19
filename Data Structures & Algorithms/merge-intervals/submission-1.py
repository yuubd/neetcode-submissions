class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            incoming = intervals[i]
            if curr[0] <= incoming[1] and incoming[0] <= curr[1]: # this assumes the intervals are sorted
                curr = [min(curr[0], incoming[0]), max(curr[1], incoming[1])]
            elif curr[1] < incoming[0]:
                res.append(curr)
                curr = incoming
            i += 1
        res.append(curr)
        return res