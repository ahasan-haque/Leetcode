class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = set()
        result = 0

        while right <= len(s) -1:
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        return result
