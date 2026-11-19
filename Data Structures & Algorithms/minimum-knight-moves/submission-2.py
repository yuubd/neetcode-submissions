class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        5:32 stopped at 6:15
           Brute force is to bfs all next positions and repeat until popped pos is. x, y O(8^n)=time and O(n^2) for space
           
           A lil optimization is so start from x,y and 0,0 expand the next kight positions with steps so visited set will be set((x, y, steps)) and update the steps only when less and if not, dont push to the queue anymore. This will reduce te time comp to O(n^2)

           or we can use min heap to add (distance to the dest, x, y) and only proceed with the least distance first. 

           states:
                dirs: 8 way
                heap: (distance to dest, current # of steps taken to x, y, x, y)
            

            add (dist from 0,0, 0, 0,0)
            while q
                heappop curr pos
                if not visited:
                    add to visited
                if at dest, return the steps
                for each dir, 
                    add to heap with +1 steps and new distance
            # shouldnt exit while
        '''      
        x, y = abs(x), abs(y) # no need of - same thing...
        visited = set([(0,0)]) # (x,y)
        q = deque([(0, 0, 0)])
        dirs = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
        while q:
            steps, x0, y0 = q.popleft()
            if x0 == x and y0 == y:
                return steps
            for dx, dy in dirs:
                nx, ny = x0+dx, y0+dy
                if (nx, ny) in visited:
                    continue
                visited.add((nx,ny))
                q.append((steps+1, nx, ny))
        return 0

    
