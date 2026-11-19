class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        => sort the hand
        => put in a map counter 
        => for total/groupsize for the group size 
        => find the smallest curr from the hand
        => while looping through, update curr += 1 and see if it can be found from the coutner, if not found, return False immediately
        => decrement the counters
        => if see any negative coutner, return False
        => return True after loop
        '''
        if len(hand) % groupSize != 0: 
            return False

        hand.sort()
        counter = defaultdict(int)
        for n in hand: counter[n] += 1
        # or just counter = Counter(hand)

        # [123 567] 3, 0 => 3
        # [1122] 2, 0 => 1
        for i in range(len(hand)):
            curr = hand[i]
            if curr not in counter or counter[curr] == 0:
                continue
            for _ in range(groupSize):
                
                if curr not in counter:
                    return False
                
                counter[curr] -= 1
                # print(counter)
                if counter[curr] < 0:
                    return False

                curr += 1
            

        return True


        


