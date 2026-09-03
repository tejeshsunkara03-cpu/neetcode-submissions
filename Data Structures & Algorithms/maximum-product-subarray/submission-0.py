class Solution:
    def maxProduct(self, nums):
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]

        for num in nums[1:]:
            temp = curMax

            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * temp, num * curMin)

            result = max(result, curMax)

        return result