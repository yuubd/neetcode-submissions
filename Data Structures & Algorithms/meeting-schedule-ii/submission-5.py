"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        
        intervals.sort(key=lambda inv: inv.start)

        endTimeHeap = [] # this is also meetings in progress
        maxConcurrentMeetings = 0
        for currIntv in intervals:
            currStart, currEnd = currIntv.start, currIntv.end
            if len(endTimeHeap) > 0 and endTimeHeap[0] <= currStart: # << this has to be <= meaning when they touch, it s not overlapping so must pop
                heapq.heappop(endTimeHeap)
            heapq.heappush(endTimeHeap, currEnd) # adding one meeting and will end at currEnd
            # print(endTimeHeap)
            maxConcurrentMeetings = max(maxConcurrentMeetings, len(endTimeHeap))
        return maxConcurrentMeetings










