from functools import lru_cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, total: int) -> int:
            if i == len(nums):
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
        
        return dfs(0, 0)