class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        '''
        9:38

        sort intervals and toBeRemoved
        1. to find the overlapping intervals from toBeRemoved
            if find any, add the cut range to res if not fully overlapped
        2. move toBeRemoved when toBeRemoved end <= interval start 
        3. do it until one of list's end is reached.
        4. if there are remaining in intervals, append

        |-----|
                |------ < remove

        |-----|
           |------ < remove

            |-----|
        |-------------| < remove

        |-----|
        |-----| < remove
        
            |-----|
        |-----| < remove

        |--------------|
            |-----| < remove
        
              |---|
        |-----| < remove
        '''
        res = []
        i = 0
        removeStart, removeEnd = toBeRemoved
        for j, [start, end] in enumerate(intervals):
            if start < removeEnd: # They overlap
                if start < removeStart:
                    res.append([start, min(end, removeStart)])
                if removeEnd < end:
                    res.append([removeEnd, end])
            else:
                res.append([start, end])
        
        return res




        
        res = []

        i = 0
        removeStart, removeEnd = toBeRemoved
        for j, [start, end] in enumerate(intervals):
            if start < removeEnd: # They overlap
                if start < removeStart:
                    res.append([start, removeStart])
                if removeEnd < end:
                    res.append([removeEnd, end])
            else:
                i += 1
                if i < len(toBeRemoved):
                    removeStart, removeEnd = toBeRemoved[i]
                else: # no more to be removed. break and append the rest
                    i = j
                    break
        
        for intv in intervals[i:]:
            res.append(intv)
        return res