class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
        nums[:] = seen
        return len(seen)