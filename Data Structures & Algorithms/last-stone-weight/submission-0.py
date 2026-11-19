class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) >= 2:
            h1 = heapq.heappop(h)
            h2 = heapq.heappop(h)

            diff = -(abs(h1-h2))
            if diff != 0:
                heapq.heappush(h, diff)
        
        return -h[0] if len(h) > 0 else 0