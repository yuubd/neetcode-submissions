class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        1:19 2:00

        [3 4 3 4 3] => 5
        [1 2 5 3 6 4 3 3] => 2 5 3 6 4 3 => 7

        no tubulance increasing or decreasing ordered arr or empty arr, it s 0
        
        brute force
            for each n, 
                check tubulance from the n O(n^2)
        
        Sliding window
            state = l, r
            maxTubulance
            starting from l = r = 0
            next = "" # SMALLER or LARGER
            while r < len(arr)
                if r > 1: 
                    if arr r -1 < arr r and next == larger:
                        next = smaller
                    if arr r -1 > arr r and next == smaller:
                        next = bigger
                    else:
                        move l to r
                        next = Smaller if arr r -1 < arr r else Larger                
                store the max from the size r-l+1

                r += 1
            return the maxT
        '''
        if len(arr) <= 1:
            return len(arr)

        l = r = 0
        maxTubulance = 1
        direction = "" # "", SMALLER, LARGER

        while r < len(arr):
            if r > 0:
                # we only have two we have can preceed
                if arr[r-1] < arr[r] and (direction == "BIGGER" or direction == ""):
                    direction = "SMALLER"
                elif arr[r-1] > arr[r] and (direction == "SMALLER" or direction == ""):
                    direction = "BIGGER"
                elif arr[r-1] == arr[r]: 
                    direction = ""
                    l = r
                else: 
                    # the direction is the issue.
                    # meaning arr[r-1:r] are in tubulance with a flipped dir
                    # going to next, we need to flip the dir again 
                    # so it s a filp of a flip = unchanged
                    # direction = unchanged
                    l = r-1

            
            maxTubulance = max(maxTubulance, r-l+1)
            r += 1        
        
        return maxTubulance
















