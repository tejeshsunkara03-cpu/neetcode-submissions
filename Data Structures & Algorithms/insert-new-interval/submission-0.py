class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Case 1: current interval is completely before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Case 2: current interval is completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # Case 3: current interval overlaps with newInterval
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res