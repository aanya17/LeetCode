class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for x in nums:
            xor = xor ^ x
        if xor != 0:
            return n
        is_zero = True
        for num in nums:
            if num != 0:
                is_zero = False
                break
        if is_zero:
            return 0
        return n - 1
        
        # return nums[1]