class Solution:
    def checkDivisibility(self, n: int) -> bool:
        suming = 0
        prod = 1
        original = n
        while n > 0:
            d = n % 10
            n = n // 10
            suming = suming + d
            prod = prod * d
        return original % (suming + prod) == 0