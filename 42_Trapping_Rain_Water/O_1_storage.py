class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_peak = height[left]
        right_peak = height[right]

        trap_unit = 0

        while left <= right:
            if left_peak < right_peak:
                trap_unit += max(left_peak - height[left], 0)
                left_peak = max(left_peak, height[left]) 
                left += 1
            else:
                trap_unit += max(right_peak -height[right], 0)
                right_peak = max(right_peak, height[right])
                right -= 1

        return trap_unit
