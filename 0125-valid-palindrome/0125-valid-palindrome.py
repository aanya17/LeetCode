class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ""
        for char in s:
            if char.isalnum():
                words = words + char.lower()
        return words == words[::-1]
        