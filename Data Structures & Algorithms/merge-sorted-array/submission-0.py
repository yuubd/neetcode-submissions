class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        sortedNums = sorted((nums1[:len(nums1)-len(nums2)] + nums2))

        for i, n in enumerate(sortedNums):
            nums1[i] = n
        