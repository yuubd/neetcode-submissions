class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        before_overlap = 0
        after_overlap = 0

        while i < len(intervals):
            s1, e1 = intervals[i]
            s2, e2 = newInterval
            # if incoming and new touch, break
            if s2 <= e1:
                break
            i += 1
        before_overlap = i

        while i < len(intervals):
            s1, e1 = intervals[i]
            s2, e2 = newInterval
            # if incoming and new dont touch, break
            if e2 < s1: 
                break

            if s1 <= e2 and s2 <= e1: # overlap, merge
                newInterval = [min(s1, s2), max(e1, e2)] 
            i += 1
        after_overlap = i

        return (intervals[:before_overlap] + 
               [newInterval] + 
               intervals[after_overlap:])