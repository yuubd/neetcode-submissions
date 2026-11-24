class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        adj matrics
        find for the one who has non in the val,
        check in other keyval and the one is in all of the others
        '''

        trustAdj = {i: set() for i in range(1, n+1)} # {person: people who trust the person}

        for p, trust in trust:
            trustAdj[trust].add(p)
        
        fullTrustees = []
        for trustee, trusters in trustAdj.items():
            if len(trusters) == n-1:
                fullTrustees.append(trustee)
        
        print(trustAdj)
        if len(fullTrustees) != 1:
            return -1
        
        fullTrustee = fullTrustees[0]
        for trustee, trusters in trustAdj.items():
            if fullTrustee in trusters:
                return -1
        
        return fullTrustee

