class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        '''
        h = []

        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]







































        h = [-n for n in nums]
        heapq.heapify(h)

        for _ in range(k):
            val = heapq.heappop(h)
        
        return -val
