class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        before_merge = 0
        after_merge = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        before_merge = i

        while i < len(intervals) and intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])] 
            i += 1
        after_merge = i

        return intervals[:before_merge] + [newInterval] + intervals[after_merge:]





