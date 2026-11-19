class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [1, 1, 1]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            res = [max(res[0], t[0]), max(res[1], t[1]), max(res[2], t[2])]
            if res == target: 
                return True
        return False
        