class HitCounter:

    def __init__(self):
        self.times = []

    def hit(self, timestamp: int) -> None:
        self.times.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        targetTime = max(timestamp - 300, 0)
        l, r = 0, len(self.times)-1 

        frmIdx = len(self.times) # no -1 to exclude all
        while l <= r: # we want to ret the one right idx of the target time 
            mid = (l+r) // 2
            midTime = self.times[mid]
            if targetTime < midTime:
                frmIdx = mid
                r = mid - 1    
            else: # midTime <= targetTime
                l = mid + 1
        return len(self.times) - frmIdx


'''
11:24 -> 11:44
There can be multiple in same time
The range is (] so including from (time-300 to everything

An index is required a list so I can access with index and run a BS O(log n) and sum up the conter O(300)
space will be a waste. 
or we can keep track of the counter and decrement on every getHits 
hit is to 
or actually we can just add to a list with duplicates and return the len(list[a:])

States
    self.times = [] # stores the times when hit
    hit: will appends the time to times

    get hits: will run a BS and get the last idx we see from curr time - 300 exclusively

    timewise: hit=O(1), getHits(log n)
    spacewise: hit=O(n), getHits(1)

'''
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
