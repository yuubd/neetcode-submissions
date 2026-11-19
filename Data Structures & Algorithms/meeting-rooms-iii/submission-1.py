class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        bf: 
        sort the meetings first, get max time
        from 0 to max time,
            check if any room is <= curr time, 
            if so add the meeting fo the room list and increment the count in another list
            remove any room whose end time < curr timm
            if the list is full and another meeting needs to start, delay the meeting by summing the 
            next ending time - the start time to start and end time of the meeting and add that in the heap
        time: O(tn*n) time * search on meetings in meetings * search on the meeting in progess list.
        space: O(n) for storing the progress list and the counter 

        '''

        meetings.sort()
        availables = [i for i in range(n)]
        using = [] # (endtime, room)
        counts = [0] * n

        for start, end in meetings:
            while using and using[0][0] <= start: # the meeting in progress has ended 
                _, freeRoom = heapq.heappop(using)
                heapq.heappush(availables, freeRoom)
            if len(availables) == 0:
                nextEndTime, room = heapq.heappop(using) # this is actually saying we are going to the nextEndTime now
                end = nextEndTime + (end-start) # start = nextEndTime, end = nextEndTime + (end-start) the interval from the new start(nextEndTime). we just dont need to update start time.
                heapq.heappush(availables, room)
            
            # if there are available rooms, pop one room, push with the endTime and increment
            room = heapq.heappop(availables)
            heapq.heappush(using, (end, room))
            counts[room] += 1

        return counts.index(max(counts))
            





        