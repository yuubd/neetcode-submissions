class NumMatrix:

    '''
    3:40
    BF is to run the 2d sum on the bounds.
    time = O(n^2)
    space = O(1)

    optimal
    compute the prefix sum of the rows,
    from prefixsum at start row1 to end row2, 
        sum the sum from col1 to col2
    return
    '''

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.prefixSumsList = [[0] * self.COLS for _ in range(self.ROWS)]
        
        for r in range(self.ROWS):
            prefix = 0
            for c in range(self.COLS):
                sumAbove = self.prefixSumsList[r-1][c] if r > 0 else 0
                prefix += matrix[r][c]
                self.prefixSumsList[r][c] = sumAbove + prefix
                
        print(self.prefixSumsList)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRight = self.prefixSumsList[row1 - 1][col2] if row1 > 0 else 0
        botLeft = self.prefixSumsList[row2][col1 - 1] if col1 > 0 else 0
        topLeft = self.prefixSumsList[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        botRight = self.prefixSumsList[row2][col2]
        return botRight - botLeft - topRight + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)