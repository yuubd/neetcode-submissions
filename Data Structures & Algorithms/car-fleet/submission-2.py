class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        create tuple list for posistion and speed
        we need to sort the positions by position
        get a list of how many rounds each car needs to get to the destination

        [1 1 12 7 3]
        [12 3 7 1 1]
        pop and while the next pop is equal or less than the curr, continue
        increment 1 in res and move on
        '''
        pos_sp = [[p, speed[i]] for i, p in enumerate(position)]
        pos_sp.sort(key=lambda x: x[0])
        print(pos_sp)

        rounds = [(target-p)/s for p, s in pos_sp]
        print(rounds)

        res = 0
        while rounds:
            curr_r = rounds.pop()
            while rounds and rounds[-1] <= curr_r:
                rounds.pop()
            res += 1
            

        return res