class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        nums1 = [3 2]
        nums2 = [1 0 3 3 4 2 1]
        find the next greater than 3 and 2
        when pop from the stack, check the num1IdxDict, if exists, append into res at nums1IdxDict[popped]


        '''
        num1IdxDict = {n:i for i, n in enumerate(nums1)}
        
        res = [-1] * len(nums1)
        st = []
        for i, n1 in enumerate(nums2):
            while st and st[-1] < n1:
                n = st.pop()
                if n in num1IdxDict:
                    res[num1IdxDict[n]] = n1
            st.append(n1)
        return res


        '''
        for each i n in nums1
            find j
            find the next greater from j to the end.
            if not found append -1
        '''
        num2IdxDict = {n:i for i, n in enumerate(nums2)}
        num1AndJs = [(num2IdxDict[n], n) for n in nums1]
        
        # BF
        res = []
        for j, n1 in num1AndJs:
            for idx in range(j, len(nums2)):
                if n1 < nums2[idx]:
                    res.append(nums2[idx])
                    break
            else:
                res.append(-1)

        return res
