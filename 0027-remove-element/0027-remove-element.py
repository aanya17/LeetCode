class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0
        # for num in nums:
        #     if num != val:
        #         nums[k] = num
        #         k += 1
        # return k
         #or
        result = []
        for num in nums:
            if num != val:
                result.append(num)
        nums[:] = result
        return len(result)