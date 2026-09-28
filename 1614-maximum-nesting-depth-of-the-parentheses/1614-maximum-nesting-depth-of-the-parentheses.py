class Solution:
    def maxDepth(self, s: str) -> int:
        ans, brackets = 0, 0
        for c in s:
            if c == '(':
                brackets += 1
            elif c == ')':
                brackets -= 1
            ans = max(ans, brackets)
        return ans