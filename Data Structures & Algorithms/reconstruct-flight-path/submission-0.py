from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):

        graph = defaultdict(list)

        for start, end in tickets:
            graph[start].append(end)

        for airport in graph:
            graph[airport].sort(reverse=True)

        result = []

        def dfs(airport):

            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]