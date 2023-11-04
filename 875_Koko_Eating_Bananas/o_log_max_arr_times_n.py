import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile
        res = max_pile
        while left <= right:
            k = (left + right) // 2
            hours_needed = sum(math.ceil(i/k) for i in piles)
            if hours_needed <= h:
                res = min(res, k) 
                right = k - 1
            else:
                left = k + 1
        return res
            