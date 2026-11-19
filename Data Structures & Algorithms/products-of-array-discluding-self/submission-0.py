class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [0  1 2 3 4]
        [24 0 0 0 0]

        get product of all in a loop anyways
        if a zero is found during the first loop, loop through and the product will only fill in for the zero's index, others will be zero
        if more than 2 zeros, doesnt matter, it s all zeros

        if no zero is found, product/nums[i]
        '''
        res = [0] * len(nums)
        zeros = 0
        zeroIdx = 0
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
                zeroIdx = i
                if zeros == 2:
                    return res 
                continue
            product *= n
        print("product:", product)
        print("res:", res, "zeroIdx:", zeroIdx)
        if zeros == 1:
            res[zeroIdx] = product
            return res
        else:
            for i, n in enumerate(nums):
                res[i] = int(product/nums[i])
        return res
            
