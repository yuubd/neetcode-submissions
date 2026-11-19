class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        skips = []
        count = 0
        curr = intervals[0]
        for incoming in intervals[1:]:
            # intervals are sorted, so curr[0] <= incoming[0] 
            # so no need to check curr[0] < incoming[1]
            if incoming[0] < curr[1]:
                count += 1 # something overlaps, we increment the count anyways
                
                # if curr[1] < incoming[1]: # incoming end is larger. curr is stil curr
                #     pass
                # else:
                curr = curr if curr[1] < incoming[1] else incoming
                
            else:
                curr = incoming

        return count


            
