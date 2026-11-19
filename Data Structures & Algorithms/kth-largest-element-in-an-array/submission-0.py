class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)

        for _ in range(k):
            val = heapq.heappop(h)
        
        return -val
