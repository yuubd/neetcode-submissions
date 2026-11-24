class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        to = len(s)//2

        for i in range(to):
            s[i], s[-1-i] = s[-1-i], s[i]