class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        8:10 
        Sort the intervals start
        if overlapping meetings > n, delay the meetings
        heap by end time and room of in grogress meetings []
        lowest rooms availables in heap initilize with from 0 to n-1
        counter for the rooms 0 * n
        for each start end of meetings:
            while inprogress.end <= start: # when we are at the next meeting start time
                pop from inprogress
                and append the room to available rooms
            if the in grogress meetings heap size >= n
                delay the meetings end time to nextEndTime + end - start
                append that to the end time heap, so dont need the start time << we do it below
                pop the next ending meeting and push the room to available
            append (endtime, get the next availavble room #) to inprogress heap
            incremenet the count
        return counter.index(max(counter))
        '''

        busyRooms = [] # min heap (endTime, room #)
        freeRooms = [i for i in range(n)] # min heap room #
        counter = [0] * n

        for start, end in sorted(meetings, key = lambda m: m[0]):
            while len(busyRooms) > 0 and busyRooms[0][0] <= start: # we are at curr start time pop all ended
                _, freeRoom = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms, freeRoom)
            if len(busyRooms) >= n:
                nextEnd, freeRoom = heapq.heappop(busyRooms)
                end = nextEnd + (end - start)
                heapq.heappush(freeRooms, freeRoom)
            freeRoom = heapq.heappop(freeRooms)
            heapq.heappush(busyRooms, (end, freeRoom))
            counter[freeRoom] += 1
            # print(busyRooms, counter) 

        return counter.index(max(counter))

















    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
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
            





        