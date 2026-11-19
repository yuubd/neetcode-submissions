class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSums = []

        summ = 0
        for n in self.nums:
            summ += n
            self.prefixSums.append(summ)
        # print(self.prefixSums)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSums[right]
        leftSum = self.prefixSums[left-1] if left else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)