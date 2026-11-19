class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
                


                
                    

        