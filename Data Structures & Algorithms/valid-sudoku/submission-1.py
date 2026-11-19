class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        3 loops
        1. validate rows
        2. validate cols
        3. validate suboard

        for each row. validate if there is any duplicate, same for col and subb
        row = board[i][j] where i is fiexd
        col = board[i][j] where j is fixed
        subboard = board[i/3][j/3]
        '''

        # validate rows
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                n = board[i][j]
                if n in s and n != ".":
                    print("return on row", s, n)
                    return False
                s.add(n)
        
        # validate col
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                n = board[j][i]
                if n in s and n != ".":
                    print("return on col", s, n)
                    return False
                s.add(n)        
        
        # validate sub-board
        '''
        00 01 02 03 04 05 06 07 08
        10 11 12 13 14 15 16 17 18
        20 21 22 03 04 05 06 07 08
        30 31 32 33 34 35 36 37 38
        40 41 42 43 44 45 46 47 48
        50 51 52 53 54 55 56 57 58
        60 61 62 63 64 65 66 67 68
        70 71 72 73 74 75 76 77 78
        80 81 82 83 84 85 86 87 88
        '''
        
        '''
        00 01 02 [[set set set]
        10 11 12  [set set set]
        20 21 22  [set set set]]
        '''
        sub_bs = [[set() for _ in range(3)] for _ in range(3)]
        print(sub_bs)

        for i in range(len(board)):
            r = int(i/3)
            for j in range(len(board)):
                c = int(j/3)
                # print("r:", r, "c:", c)
                s = sub_bs[r][c]
                n = board[i][j]
                if n in s and n != ".":
                    return False
                s.add(n)
                
                

        return True





