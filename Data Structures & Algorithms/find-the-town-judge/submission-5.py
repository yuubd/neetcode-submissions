class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        adj matrics
        find for the one who has non in the val,
        check in other keyval and the one is in all of the others
        '''

        trustAdj = defaultdict(int)

        for src, dest in trust:
            trustAdj[dest] += 1 # src trusts dest out bound
            trustAdj[src] -= 1 # src cant be the judge
        
        for trustee, trusters in trustAdj.items():
            if trusters == n-1:
                return trustee
        return -1