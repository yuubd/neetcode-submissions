class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        this is to minimize all numbers to same num

        Even numbers can decrease
        odd numbers can increase,

        so the target low odd numbers 
        
        need to match close to the high odd
        or low even

        [3,6] target is 3 or 6

        decreasing can be done multiple time but increasing is alsways max one time cuz any number * 2 is odd

        *2 all odd numbers so we check the all *2 cases
        add the values to max heap and /2 and then check the deviation, so on until there is nothing to /2
        return the tracked deviation

        '''

        nums = [n * 2 if n % 2 == 1 else n for n in nums ]
        smallest = min(nums)
        deviation = float("inf")

        h = [-n for n in nums]
        heapq.heapify(h) # here all values are even
        while True:
            largest = -heapq.heappop(h)
            deviation = min(deviation, largest - smallest)
            if largest % 2 == 1: # the largest is odd = we have /2 all possible values
                break
            
            heapq.heappush(h, -largest // 2)
            smallest = min(smallest, largest // 2)


        return deviation
        






