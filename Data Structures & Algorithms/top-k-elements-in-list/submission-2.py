class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Need a counter map. And the reverse counter
        from n to 1, add numbers to res array until the len is == k
        '''

        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        print(d)
    
        rev_d = defaultdict(list[int])
        for n, c in d.items():
            rev_d[c].append(n)
        print(rev_d)

        res = []
        for i in range(len(nums), 0, -1): # start, stop before, step
            if i in rev_d:
                for n in rev_d[i]:
                    res.append(n)
                    if len(res) == k:
                        return res 
                
        return res