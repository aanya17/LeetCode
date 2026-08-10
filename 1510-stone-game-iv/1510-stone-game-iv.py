# import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # if n == 1 or math.sqrt(n).is_integer():
        #     return True
        # return False
        dp = [False] * (n+1)
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]
