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
        self.prefixSumsList = [[0] * (self.COLS+1) for _ in range(self.ROWS+1)]
        
        for r in range(self.ROWS):
            prefix = 0
            for c in range(self.COLS):
                sumAbove = self.prefixSumsList[r][c+1]
                prefix += matrix[r][c]
                self.prefixSumsList[r+1][c+1] = sumAbove + prefix
                
        print(self.prefixSumsList)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRight = self.prefixSumsList[row1][col2+1]
        botLeft = self.prefixSumsList[row2+1][col1]
        topLeft = self.prefixSumsList[row1][col1]
        botRight = self.prefixSumsList[row2+1][col2+1]
        return botRight - botLeft - topRight + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)