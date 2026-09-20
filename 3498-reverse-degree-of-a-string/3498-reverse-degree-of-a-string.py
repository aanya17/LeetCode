class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, char in enumerate(s):
            reverse_position = 26 - (ord(char) - ord('a'))
            string_position = i + 1
            ans += reverse_position * string_position
        return ans