class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        for each i n in nums1
            find j
            find the next greater from j to the end.
            if not found append -1
        '''

        num2IdxDict = {n:i for i, n in enumerate(nums2)}
        num1AndJs = [(num2IdxDict[n], n) for n in nums1]
        print(num1AndJs) # [2 4, 0 1, 3 2]
        
        res = []
        for j, n1 in num1AndJs:
            for idx in range(j, len(nums2)):
                if n1 < nums2[idx]:
                    res.append(nums2[idx])
                    break
            else:
                res.append(-1)

        return res
