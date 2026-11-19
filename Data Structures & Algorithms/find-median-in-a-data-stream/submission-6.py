class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.lst)-1

        resIdx = -1
        while l <= r:
            mid = (l+r) // 2
            if num < self.lst[mid]:
                r = mid - 1
            else:
                resIdx = mid
                l = mid + 1
        # print(num)
        # print(self.lst)
        # print(resIdx)
        self.lst = self.lst[:resIdx+1] + [num] + self.lst[resIdx+1:]

    def findMedian(self) -> float:
        isEven = len(self.lst) % 2 == 0
        
        mid = (len(self.lst)-1) // 2
        # print("findMedian", self.lst, "mid", mid)
        if isEven:
            return (self.lst[mid] + self.lst[mid+1]) / 2
        else:
            return self.lst[len(self.lst) // 2]

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