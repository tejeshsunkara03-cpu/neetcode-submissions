from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()

        for i, n in enumerate(nums):

            while q and nums[q[-1]] < n:
                q.pop()

            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                output.append(nums[q[0]])

        return output