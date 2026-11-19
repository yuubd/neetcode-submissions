class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = defaultdict(lambda: defaultdict(lambda: defaultdict(set))) # whats defaultdict of defaultdict 

    '''
    6:03 -> 6:48
    board = a board of 0s
    player 1 = 1 and player 2 =2
    cell are guarenteed to be valid

    move:
        brute force:
            need to update the board, wondering if we need a physical board
            scan the board and return 1 or 2 if the condition is met.
            time: O(n^2)
            space: O(n^2)
        
        more optimal
            dict
                1: {
                    {row: set(cols)} # might not need to store each pos if we are guarenteed same pos will not be called
                    {col: set(row)},
                    {diag: set([r,c])}
                2: [set(cols), set(rows), set(dia)]
            check if any set len is len of n
            
            time: O(1)
            space: O(n^2)
            
            n = 2
            for player 1: 00 01 => 1
                dicr[1]["rows"][0].add(1)
                dicr[1]["cols"][1].add(0)
                dicr[1]["diag"].add(0) if r c are equal
            if one of len of one of them is n, return the player id
    '''
    def move(self, row: int, col: int, player: int) -> int:
        # {rows:.., cols:..., diag:...}
        playerDict = self.board[player]
        # print(playerDict)

        # add to board
        playerDict["rows"][row].add(col)
        playerDict["cols"][col].add(row)
        if row == col: # diag[0] is for normal diagonal, diag[1] is reverse diagnoal
            playerDict["diag"][0].add((row, col))
        if row + col + 1 == self.n:
            playerDict["diag"][1].add((row, col))
        
        # validate
        for row, colSet in playerDict["rows"].items():
            if len(colSet) == self.n:
                return player
        
        for col, rowSet in playerDict["cols"].items():
            if len(rowSet) == self.n:
                return player
        
        if len(playerDict["diag"][0]) == self.n or len(playerDict["diag"][1]) == self.n:
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)



