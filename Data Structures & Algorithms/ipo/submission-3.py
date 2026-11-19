class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        12:27
        We need to couple the profit and capital together,
        amound avilable projects, we need to take the project with the maximum profit

        states:
            1. projects: A heap or sort the projects [capital, profits]
            2. availables: A heap to store the maximum profits [profits]
            * no need to keep the indices as we dont need to return the idx
            
            make the first heap
            while count or the res len is < k:
                add all projects to the availables if caital <= w
                pop the most profitable project from the availables
                update w
            
            return w

        eg. k=3, w=2, profit=[2 3 6 1 1], capital=[1 2 5 4 0]
        projects = [4 1] [5 6] 
        availables = [2] [1]
        
        projedts = []
        availables = 2 1 1 
        
        w=2+3+6 = k many
        return 
        '''

        projects = []
        for i in range(len(profits)):
            heapq.heappush(projects, (capital[i], profits[i]))

        availables = []
        count = 0
        while count < k:
            while projects and projects[0][0] <= w:
                capital, profit = heapq.heappop(projects)
                heapq.heappush(availables, -profit)
            # print('w, availables', w, availables)
            
            if not availables:
                return w
            mostProfit = heapq.heappop(availables)
            count += 1
            w += -mostProfit

        
        return w










