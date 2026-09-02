from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = defaultdict(list)

        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        heap = [(0, src, 0)]

        best = {}

        while heap:

            price, node, flights_taken = heapq.heappop(heap)

            if node == dst:
                return price

            if flights_taken == k + 1:
                continue

            for nei, cost in adj[node]:

                new_price = price + cost
                new_flights = flights_taken + 1

                if (
                    (nei, new_flights) not in best
                    or new_price < best[(nei, new_flights)]
                ):

                    best[(nei, new_flights)] = new_price

                    heapq.heappush(
                        heap,
                        (new_price, nei, new_flights)
                    )

        return -1