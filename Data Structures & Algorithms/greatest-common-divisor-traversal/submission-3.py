class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        '''
        consider each nums[i] as a node
        there is an edge if gcd(nums[i], nums[j]) > 1
        
        I need to create a node adjacency list for each node and run a any traversal algo to see if all nodes can be visited.
        '''
        from math import gcd
        n = len(nums)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):# !!! for j, n2 in enumerate(nums[i+1:]): j starts from 0
                if gcd(nums[i], nums[j]) > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == len(nums):
                return True
            
            adjs = adj[node]
            for nxtNode in adjs:
                q.append(nxtNode)

        return False 






