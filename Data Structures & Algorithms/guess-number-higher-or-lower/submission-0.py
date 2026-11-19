# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while True:
            candidate = int((start+end)/2)
            guessed = guess(candidate)
            if guessed == 0: return candidate
            if guessed == -1: end = candidate-1
            else: start = candidate+1
        