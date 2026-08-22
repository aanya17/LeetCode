class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m] + nums2
        temp.sort()
        nums1[:] = temp