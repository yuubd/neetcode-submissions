class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = defaultdict(int)
        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []
        curr_end_idx = 0
        start = 0
        for i, c in enumerate(s):
            curr_end_idx = max(curr_end_idx, last_idx[c])
            if i == curr_end_idx:
                res.append(curr_end_idx - start + 1)
                start = i + 1

        return res
            

