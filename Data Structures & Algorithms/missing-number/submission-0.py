class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result ^= i
            result ^= nums[i]

        return result