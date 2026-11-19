class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Eulerian path: where nodes can be visited multiple times but only once for edges.
        I want to find the path to use all edges.
        * Lexicographical order
        Hierholzer
        states
        adjMap scr: destinations sorted and reversed
        output which is len of tickets + 1

        def dfs src
            if path len is n:
                return
            while adj of src is not empty
                dfs(adj list pop())
            output.append(src)
        return output
        '''

        adjMap = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            adjMap[src].append(dest)
        
        n = len(tickets) + 1
        output = []
        def dfs(src):
            if len(output) == n:
                return
            while adjMap[src]:
                dfs(adjMap[src].pop())
            output.append(src)
        dfs("JFK")
        return output[::-1]



    def findItineraryDFSBacktracking(self, tickets: List[List[str]]) -> List[str]:
        # 1:22
        '''
        1. no lower case?
        2. confirming need to use all tickket once?
        3. could there be two itineraries?

        This is about using tickets.
        The sol could be going to any airport, so dfs with backtracking 
        states
            adj deque from sorted tickets
        
        dfs with airport path:
            if path is len of n = len of ticket + 1 return the path

            for i in the len adj list:
                pop the next airport from the list with i
                res = dfs(next, path+next)
                if res: return res
                insert the next airport back with i
            return None
        '''

        adjMap = defaultdict(list)
        for src, dst in sorted(tickets):
            adjMap[src].append(dst)
        n = len(tickets) + 1

        def dfs(airport, path):
            if len(path) == n:
                return path

            for i in range(len(adjMap[airport])):
                nextAirport = adjMap[airport].pop(i)
                res = dfs(nextAirport, path + [nextAirport])
                if res:
                    return res
                adjMap[airport].insert(i, nextAirport)

            return None

        return dfs('JFK', ['JFK'])











