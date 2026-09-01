import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append((v, t))

        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        heap = [(0, k)]

        while heap:

            currentTime, node = heapq.heappop(heap)

            if currentTime > distances[node]:
                continue

            for neighbor, time in graph[node]:

                newTime = currentTime + time

                if newTime < distances[neighbor]:

                    distances[neighbor] = newTime

                    heapq.heappush(heap, (newTime, neighbor))

        answer = max(distances[1:])

        if answer == float("inf"):
            return -1

        return answer