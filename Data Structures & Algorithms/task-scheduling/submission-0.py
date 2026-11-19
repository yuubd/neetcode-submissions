class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            11:09 stopped at 11:50
            1. we need to start from the task which there are the most
            2. we need a max heap (# of remaining, name)

            ["X","X","X,"X,"X,"Y","Y"] n = 2
            (-5 X) (-2 Y)

            state
                deque
                max heap
                res = time
            generate the heap
            while h:
                1st: X,   popped: (-4 X) h = (-2 Y) # maybe pop until the cooltime, could use deque() <= len of n
                2nd: Y,   popped: (-2 Y) h = []       deque((-3 X))
                3rd: idle popped: None   h = [(-3 X)],deque((-1 Y), (0, "IDLE")) << if h is empty, idle, continue. if  deque len == n, popleft and push. Also add Idle to deque as a placeholder.
                4th: X,   popped: (-3 X) h = (-1 Y),  deque((0, "IDLE"))
                5th: Y,   popped: (-1 Y) h = [],      deque((0, "IDLE"), (-2 X))

                increment the res time += 1 

            Brute force would trying every combination and add Idle in a separate loop, eg. X X Y Y => X I I X Y I I Y ... O(n^2)
        '''
        # generate h
        m = defaultdict(int)
        for task in tasks: m[task] += 1
        
        h = []
        for task, count in m.items(): heapq.heappush(h, (-count, task, 0)) # and time
        print(h)

        q = deque() # size is n
        cycles = 0 # is also curr time
        '''
            heap: tasks with cooledAt < currentCycles
            heap: tasks with cooledAt > currentCycles
        '''
        while h or q:
            while q and q[0][2] < cycles:
                heapq.heappush(h, q.popleft())
            
            if len(h) > 0:
                count, task, cooledAt = heapq.heappop(h) 
            
                if count < -1:
                    q.append((count+1, task, cycles + n))
                

            cycles += 1


        return cycles
        
























