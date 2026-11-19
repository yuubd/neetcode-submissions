class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        res = [-1] * len(queries)
        h = []
        j = 0
        for q, idx in sorted((q, i) for i, q in enumerate(queries)):
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(h, [r-l+1, l, r]) # len, l, r
                j += 1
            while h and not (q <= h[0][2]): # h[0][2] is hte right of an interval with shortest len
                heapq.heappop(h)
            if h:
                res[idx] = h[0][0]

        return res