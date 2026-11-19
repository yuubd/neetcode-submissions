class Solution:
    def checkValidString(self, s: str) -> bool:
        # balance_for_open/close is the bracket balance of s while considering all * as open or close
        # so when any of these balance is +/-, it means there are more open/close b whil considering all *s open/close
        balance_for_open = 0
        balance_for_close = 0

        for c in s:
            if c == "(":
                balance_for_open += 1
                balance_for_close += 1
            elif c == ")":
                balance_for_open -= 1
                balance_for_close -= 1
            else: # *
                balance_for_open += 1
                balance_for_close -= 1
            
            # Though we conver all * to (, we there are more close brackets 
            # balance_for_close < 0: << we dont need this part as if balance_for_open < 0 is True then balance_for_close < 0 is true too
            if balance_for_open < 0:  
                return False
            
            # We dont want to carry balance_for_close when the balance_for_open is >= 0. 
            # This is the greedy part. and it s always balance_for_close < balance_for_open
            if balance_for_open >= 0: # balance_for_close should be 0 or negative. Refresh
                balance_for_close = max(0, balance_for_close)
        
        # after loop, if the range contains 0, return True
        print('balance_for_open', balance_for_open)
        print('balance_for_close', balance_for_close)
        return 0 in range(balance_for_close, balance_for_open+1)













