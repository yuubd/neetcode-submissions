class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        n/3 = floor(len(nums)/3)

        There can be only two elems as it s over 33%
        '''

        d = defaultdict(int)
        for n in nums:
            if len(d) > 2:
                if d[n] == 1:
                    for k in list(d.keys()):
                        if k != n: 
                            d[k] -= 1
                        if d[k] == 0:
                            del d[k]
            else: 
                d[n] += 1
            # print(d)
        
        res = []
        for k, v in d.items():
            if nums.count(k) > int(math.floor(len(nums) / 3)):
                res.append(k)

        return res



        



