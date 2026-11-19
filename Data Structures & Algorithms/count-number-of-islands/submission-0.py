class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == True: continue
                if grid[r][c] == "1":
                    q = deque([[r,c]])
                    while len(q) > 0:
                        pos_r, pos_c = q.popleft()
                        if not(0 <= pos_r <= len(grid)-1 and 0 <= pos_c <= len(grid[0])-1):
                            continue
                        if visited[pos_r][pos_c] == True: 
                            continue
                        # print(pos_r, pos_c)
                        if grid[pos_r][pos_c] == "1":
                            # print(pos_r, pos_c)
                            q.append([pos_r-1,pos_c])
                            q.append([pos_r+1,pos_c])
                            q.append([pos_r,pos_c-1])
                            q.append([pos_r,pos_c+1])
                        visited[pos_r][pos_c] = True
                    count += 1
                visited[r][c] = True
                    
        return count