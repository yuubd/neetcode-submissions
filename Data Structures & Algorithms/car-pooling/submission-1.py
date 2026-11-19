class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        10:48
        we first need to sort the trips by the from
        for each trip, 
            while the next To <= the curr from,
                increment the capacity
            capacity = would be decremented by the passengers,
            anytime if capacity < 0: false
            We need see to keep track of the next to. Heap ToHeap [To, passengers]
            add the curr trip's To to the Heap
        return true
        '''
        
        currCap = capacity
        trips.sort(key = lambda trip: [trip[1], trip[2]]) # sort by from and to
        toHeap = []
        for passengers, frm, to in trips:
            while toHeap and toHeap[0][0] <= frm:
                nextTo, nextCap = heapq.heappop(toHeap)
                currCap += nextCap # never be greter than the original
            currCap -= passengers
            if currCap < 0:
                return False
            heapq.heappush(toHeap, [to, passengers])

        return True
            


