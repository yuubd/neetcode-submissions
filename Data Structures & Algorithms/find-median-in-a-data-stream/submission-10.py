class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        '''
        if lower is empty or num <= lower[0]
        add to lower with -

        otherwise, add to upper

        if len are diff by 2, then balance
        '''

        if len(self.lower) == 0 or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        
        if abs(len(self.upper) - len(self.lower)) > 1:
            if len(self.upper) > len(self.lower):
                heapq.heappush(self.lower, -heapq.heappop(self.upper))
            else:
                heapq.heappush(self.upper, -heapq.heappop(self.lower))

        
    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            return (self.upper[0] + -self.lower[0]) /2
        else:
            return self.upper[0] if len(self.upper) > len(self.lower) else -self.lower[0]







class MedianFinder1:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.nums)-1

        resIdx = len(self.nums) # not -1 becauase len(self.nums) will not include the last n in self.nums[:resIdx]
        while l <=r:
            mid = (l+r) // 2
            if num <= self.nums[mid]:
                resIdx = mid
                r = mid - 1
            else:
                l = mid + 1
        self.nums = self.nums[:resIdx] + [num] + self.nums[resIdx:]

    def findMedian(self) -> float:
        isEven = len(self.nums) % 2 == 0
        
        mid = (len(self.nums)-1) // 2
        # print("findMedian", self.nums, "mid", mid)
        if isEven:
            return (self.nums[mid] + self.nums[mid+1]) / 2
        else:
            return self.nums[len(self.nums) // 2]

'''
3 2 4 4 1
3 => 3
2 3 => 2.5
2 3 4 => 3
2 3 4 4 =? 3.5
1 2 3 4 4 => 3
'''     
'''
we wanna store the numbers sorted.
use heap to keep it sorted
states
    h [] = use heapq to store

addNum
    add the num to the heap

findMedian
    isEven = len of h mod 2 == 0
    get the mid and mid+1 nums and / 2

    return the mid n
'''