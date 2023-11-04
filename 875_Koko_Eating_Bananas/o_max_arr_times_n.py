import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        for k in range(1, max_pile+1):
            hours_needed = sum(math.ceil(i/k) for i in piles)
            if hours_needed <= h:
                return k

