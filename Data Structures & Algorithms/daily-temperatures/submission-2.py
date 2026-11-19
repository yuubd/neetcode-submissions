class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0] * len(temperatures)

        st = []
        curr_tmp = 0
        for i, t in enumerate(temperatures):
            while len(st) > 0 and t > st[-1][1]:
                res[st[-1][0]] = i-st[-1][0]
                st.pop()
            st.append([i,t])
        return res



    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        '''
        Have a default list for the len of temps
        For each t, 
            check if the first (not pop) t in the st is lower,
            if so, add curr_t.idx-last_t.idx+1 and pop
            append in the st [t, idx]
        return the res
        '''
        res = [0] * len(temperatures)
        st = [] # pair: [idx, t]
        for idx, t in enumerate(temperatures):
            # print("idx", idx, "t", t)
            # st[-1][0] = last_t_idx
            # st[-1][1] = last_t
            while len(st) > 0 and st[-1][1] < t:
                res[st[-1][0]] = idx - st[-1][0]
                st.pop()
            st.append([idx, t])
            # print("res", res, "st", st)
        
        return res