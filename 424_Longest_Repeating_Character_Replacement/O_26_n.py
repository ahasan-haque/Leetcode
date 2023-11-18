class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0

        freq = dict()

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if right - left + 1 - max(freq.values()) <= k:
                result = max(result, right - left + 1 )
            else:
                freq[s[left]] -= 1
                left += 1
            right += 1

        return result        