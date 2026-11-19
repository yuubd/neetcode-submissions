class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Go over each n
        target = 0-n,
        excluding the n, get the target sum fromf the list
        '''

        res = {}
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        print(d)
        for i, n in enumerate(nums):
            target = 0 - n
            for j, n2 in enumerate(nums[i + 1:], start=i + 1):
                if target - n2 not in d:
                    continue
                for idx_for_n3 in d[target - n2]:
                    #print("target", target, "i", i, "n", n, "n2", n2, "idx_for_n3", idx_for_n3)
                    if idx_for_n3 == i or idx_for_n3 ==j:
                        continue
                    sorted_ans = sorted([n, n2, nums[idx_for_n3]])
                    res[str(sorted([n, n2, nums[idx_for_n3]]))] = sorted([n, n2, nums[idx_for_n3]])
                    #print(res)
        return list(res.values())