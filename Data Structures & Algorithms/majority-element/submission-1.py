class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maj = -1
        majCount = 0
        for n, c in counter.items():
            if majCount <= c:
                maj, majCount = n, c
        return maj