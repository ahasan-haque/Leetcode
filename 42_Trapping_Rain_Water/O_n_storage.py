class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost = 0
        left_peak = []
        for i in range(len(height)):
            left_peak.append(leftmost)
            leftmost = max(leftmost, height[i])

        rightmost = 0
        right_peak = [None] * len(height) 
        for i in range(len(height) -1, -1, -1):
            right_peak[i]= rightmost
            rightmost = max(rightmost, height[i])
        result = 0

        for i in range(len(height)):
            result += max((min(left_peak[i], right_peak[i]) - height[i]), 0)

        return result

