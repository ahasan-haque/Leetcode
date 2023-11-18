class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0
        max_f = 0
        freq = dict()
        '''
        Here, the trick of O(n) solution to keep a max_f is to avoid looking for max(freq.values()) in each iteration.
        max(freq.values()) is O(26), as we are dealing with only 26 characters (Uppercase English letters).
        
        adding a max_f is O(1) operation. so, the overall time complexity is O(n).

        max_f works, because (right - left + 1) - (freq[s[right]]) <= k doesn't really change if freq[s[right]] gets lower.
        So, if we add something from the right, and it's the most frequent character, we can just update max_f. If we remove 
        something from the left, it doesn't impact the overall boolean expression, so we don't need to update max_f.
        '''
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_f = max(max_f, freq[s[right]])

            if right - left + 1 - max_f <= k:
                result = max(result, right - left + 1 )
            else:
                freq[s[left]] -= 1
                left += 1
            right += 1

        return result        