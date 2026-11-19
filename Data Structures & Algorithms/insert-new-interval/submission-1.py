class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        before_overlap = 0
        after_overlap = 0

        while i < len(intervals):
            s1, e1 = intervals[i]
            s2, e2 = newInterval
            if s2 <= e1: # we only need to check 
                break
            i += 1
        before_overlap = i

        while i < len(intervals):
            s1, e1 = intervals[i]
            s2, e2 = newInterval

            if e2 < s1: # new interval is on the left.
                break

            if s1 <= e2 and s2 <= e1: # overlap
                newInterval = [min(s1, s2), max(e1, e2)] 
            i += 1
        after_overlap = i

        print(newInterval, before_overlap, after_overlap)

        return (intervals[:before_overlap] + 
               [newInterval] + 
               intervals[after_overlap:])