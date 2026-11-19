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
        self.prefixSumsList = []
        
        row = []
        for r in range(self.ROWS):
            summ = 0
            for c in range(self.COLS):
                n = matrix[r][c]
                summ += n
                row.append(summ)
            self.prefixSumsList.append(row.copy())
            row = []
        print(self.prefixSumsList)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        summ = 0
        for r in range(row1, row2+1):
            prefixSums = self.prefixSumsList[r]
            leftSum = prefixSums[col1 - 1] if col1 else 0
            rightSum = prefixSums[col2] 
            summ += (rightSum - leftSum)
        return summ

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)