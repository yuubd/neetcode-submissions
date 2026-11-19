class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        skips = []
        count = 0
        curr = intervals[0]
        for incoming in intervals[1:]:
            if incoming[0] < curr[1]:
                # intervals are sorted, so curr[0] <= incoming[0]
                if curr[1] < incoming[1]:
                    pass
                else:
                    curr = incoming
                count += 1
            else:
                curr = incoming

        return count


            
