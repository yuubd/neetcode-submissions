"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        room_count = 0
        h = []
        for curr in intervals:
            while len(h) > 0 and h[0] <= curr.start:
                heapq.heappop(h)
            heapq.heappush(h, curr.end)
            room_count = max(room_count, len(h))
        
        return room_count


