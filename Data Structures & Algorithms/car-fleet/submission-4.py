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

        rounds = [(target-p)/s for p, s in pos_sp]

        # so from the target close cars, if the car st[-2] has bigger rounds than follwing car st[-1] pop the following car meaning that car will be merged with the front car
        st = []
        for r in reversed(rounds):
            st.append(r)
            if len(st) >= 2:
                followingCarRounds = st[-1] # farther is the appeded later
                closestCarRounds = st[-2]
                if closestCarRounds >= followingCarRounds:
                    st.pop() # the following car will be merged
        return len(st) # the remaining st is the fleets


