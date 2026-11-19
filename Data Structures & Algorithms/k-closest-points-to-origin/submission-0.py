class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            mag = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(h, [mag, p[0], p[1]])
        print(h)
        return [heapq.heappop(h)[1:] for _ in range(k)]