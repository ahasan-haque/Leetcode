import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile
        while left <= right:
            mid = (left + right) // 2
            hours_needed = sum(math.ceil(i/mid) for i in piles)
            if hours_needed == h:
                return mid
            elif hours_needed < h:
                right = mid - 1
            else:
                left = mid + 1
            