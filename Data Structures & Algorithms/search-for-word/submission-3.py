class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m_y = len(board)
        n_x = len(board[0])
        visited = [[False] * n_x for _ in range(m_y)]

        def backtrack(i, y, x):
            if i == len(word):
                return True
            
            # boundary check
            if not (0 <= y < m_y and 0 <= x < n_x):
                return False
            
            if visited[y][x] == True:
                return False

            # char check
            if word[i] != board[y][x]:
                return False

            visited[y][x] = True

            # found the char
            found = (
                backtrack(i+1, y+1, x) or
                backtrack(i+1, y-1, x) or 
                backtrack(i+1, y,   x+1) or 
                backtrack(i+1, y,   x-1)
            )

            visited[y][x] = False
            return found

        for y in range(len(board)):
            for x in range(len(board[0])):
                if word[0] == board[y][x]:
                    if backtrack(0, y, x):
                        return True
        return False