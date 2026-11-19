class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Have a default list for the len of temps
        For each t, 
            check if the first (not pop) t in the st is lower,
            if so, add curr_t.idx-last_t.idx+1 and pop
            append in the st [t, idx]
        return the res
        '''
        res = [0] * len(temperatures)
        st = []
        for idx, t in enumerate(temperatures):
            print("idx", idx, "t", t)
            while len(st) > 0 and st[-1][1] < t:
                res[st[-1][0]] = idx - st[-1][0]
                st.pop()
            st.append([idx, t])
            print("res", res, "st", st)
        
        return res