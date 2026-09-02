class Solution:
    def rob(self, nums):

        rob1 = 0
        rob2 = 0

        for money in nums:

            current = max(
                rob1 + money,
                rob2
            )

            rob1 = rob2
            rob2 = current

        return rob2