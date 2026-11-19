class TimeMap:

    def __init__(self):
        self.itemMap = defaultdict(list) # map of k: [v, t]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.itemMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        '''
        do BS to find the right idx for the incoming timestamp
        if exist, return, if not, return the prev
        '''
        # print(self.itemMap)
        items = self.itemMap[key]
        l, r = 0, len(items)-1
        mid = 0
        res = ""
        while l <= r:
            mid = (l+r)//2
            val = items[mid][0]
            time = items[mid][1]
            if time == timestamp:
                return val
            if time < timestamp:
                res = val
                l = mid + 1
            else: 
                r = mid - 1


        # print(timestamp, mid)

        return res
        
