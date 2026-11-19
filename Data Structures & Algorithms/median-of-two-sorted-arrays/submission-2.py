class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        shorter, longer = (nums1, nums2) if len1 <= len2 else (nums2, nums1)
        isEven = (len1 + len2) % 2 == 0

        # halfSize is 3 is total len is 6 [123][456]
        halfSize = (len(shorter) + len(longer)) // 2

        # we will BS on shorter cuz shorter can be the whole half
        l = 0
        r = len(shorter)-1
        while True:
            # parIdxS: like mid in a regular BS
            # parIdxL: rest number of elem. halfSize - the num of left side of shorter partition
            parIdxS = (l + r) // 2 # 0+3//2=1 so two elem in shorter
            parIdxL = halfSize - parIdxS - 2 # 3-1 = 2 - 2 (as half size is not index and -1 )

            # 1. 2.
            leftOfSPartition = shorter[parIdxS] if 0 <= parIdxS else float('-inf')
            rightOfSPartition = shorter[parIdxS+1] if parIdxS < len(shorter)-1 else float('inf')
            # 3. 4.
            leftOfLPartition = longer[parIdxL] if 0 <= parIdxL else float('-inf')
            rightOfLPartition = longer[parIdxL+1] if parIdxL < len(longer)-1 else float('inf')

            # if 1.|2. 3.|4. and 1<=4 & 3 <=2, it s perfect half 
            if leftOfSPartition <= rightOfLPartition and leftOfLPartition <= rightOfSPartition:
                if isEven: 
                    return (min(rightOfSPartition, rightOfLPartition) 
                            + max(leftOfSPartition, leftOfLPartition)) / 2
                else: 
                    return min(rightOfSPartition, rightOfLPartition)
            
            # not a perfect partitiion, move l, r try again
            if not (leftOfSPartition <= rightOfLPartition):
                r = parIdxS - 1
            else:
                l = parIdxS + 1


        return 0
        











    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        is_even = total_len % 2 == 0

        S = []
        L = []
        if len(nums1) > len(nums2):
            L, S = nums1, nums2
        else:
            L, S = nums2, nums1
        
        l = 0
        r = len(S) - 1
        half_size = total_len // 2
        # BS
        while True:
            # i is the BS idx of S & j is the index for L
            i = (l + r) // 2
            j = half_size - i - 2

            # check if we found partition Left = left from partition boundary
            Sright = S[i+1] if i + 1 < len(S) else 1001
            Lright = L[j+1] if j + 1 < len(L) else 1001
            
            Sleft = S[i] if 0 <= i else -1001 
            Lleft = L[j] if 0 <= j else -1001 

            # compare
            if Sleft <= Lright and Lleft <= Sright:
                if is_even:
                    return (min(Sright, Lright) +
                            max(Sleft, Lleft)) / 2
                else:
                    return min(Sright, Lright)
            else:
                if Lright > Sleft:
                    l = i + 1
                else:
                    r = i - 1
