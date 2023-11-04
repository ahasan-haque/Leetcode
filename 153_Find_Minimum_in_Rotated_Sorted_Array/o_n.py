class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while nums[left] > nums[right]:
            left += 1
        return nums[left]
        