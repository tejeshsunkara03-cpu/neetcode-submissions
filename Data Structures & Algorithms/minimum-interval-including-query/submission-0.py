import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sorted_queries = sorted(queries)

        res = {}
        heap = []
        i = 0

        for q in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]

                length = right - left + 1

                heapq.heappush(heap, (length, right))

                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]