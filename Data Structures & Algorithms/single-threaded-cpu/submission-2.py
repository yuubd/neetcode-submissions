class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        11:46 -> 12:44
        1. need to preserve the original index
        2. heap/sort in order of enquetime, processing time, then orig index

        BF: find the lowest enqueue time task/s
            for ties, find the lowest procesing time
            replace the task with None to indicate the task is processed,
            add its index to res
            repeat until the res len if n
            time: O(n*n)
            spaece: O(n)
        
        optimal:
            So this is to find the min processing time task among availables
            heapify ^^^^ to make the loop easier
            we need to sort and a heap(avilable) to find the least processing time task
            first, append the original index to the tasks O(n) [enqueuedTime, processingTime, origIdx]
            states:
                sortedHeap = [] # [enqueuedTime, processingTime, origIdx]
                availableHeap = [] # [processingTime, orig index] dont need when avaialble. once tasks are in this heap, meaning they are available.
                
                
                while res len < n:
                    enqueuedTime, processingTime, origIdx = pop from sortedHeap if available len is 0: # meaning idle else available pop
                    res.append(origind)
                    
                    while loop:
                        need to heappush all tasks to availables with enqueuedTime + processingTime < enqueuedTime
                return res
        '''
        n = len(tasks)
        tasks = [[procTime, i, enqTime] for i, [enqTime, procTime] in enumerate(tasks)] # O(n)
        
        tasks.sort(key = lambda task: [task[2],task[0]]) # tasks = [eTime, pTime, i] O(n)
        tasks = deque(tasks)
        print(tasks)

        availables = [] # # [processingTime, orig indexm enqueuedTime]
        res = []
        currTime = 0 # MISSED the need of currTime
        while len(res) < n:
            
            procTime, origIdx, enqTime = tasks.popleft() if len(availables) == 0 else heapq.heappop(availables)
            
            res.append(origIdx)
            currTime = max(currTime, enqTime) + procTime
            while len(tasks) > 0 and tasks[0][2] <= currTime:
                heapq.heappush(availables, tasks.popleft())
        return res

        '''
        tasks = 
        ^
        [1,2,4]
        5
        availables =  [2,0,5] [4,1,4] 
        res = 3
        '''


























