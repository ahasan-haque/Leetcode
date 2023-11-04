class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 
        minimum = nums[left]

        while left <= right:
            # first check if the sub array is already sorted. If yes, immediately possible to return
            if nums[left] <= nums[right]:
                minimum = min(minimum, nums[left])
                break

            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if nums[left] <= nums[mid]:
                # equal because mid might be leftmost
                left = mid + 1
            else:
                right = mid - 1
        return minimum 