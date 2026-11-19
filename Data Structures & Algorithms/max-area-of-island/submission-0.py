class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == True: continue
                if grid[r][c] == 1:
                    q = deque([[r,c]])
                    area = 0
                    while len(q) > 0:
                        pos_r, pos_c = q.popleft()
                        if not(0 <= pos_r <= len(grid)-1 and 0 <= pos_c <= len(grid[0])-1):
                            continue
                        if visited[pos_r][pos_c] == True: 
                            continue
                        if grid[pos_r][pos_c] == 1:
                            q.append([pos_r-1,pos_c])
                            q.append([pos_r+1,pos_c])
                            q.append([pos_r,pos_c-1])
                            q.append([pos_r,pos_c+1])
                            area += 1
                        visited[pos_r][pos_c] = True
                    max_area = max(max_area, area)
                visited[r][c] = True
                    
        return max_area