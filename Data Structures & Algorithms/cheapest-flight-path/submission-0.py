from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        # Build adjacency list
        adj = defaultdict(list)

        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        # (price, airport, stops)
        heap = [(0, src, 0)]

        # Cheapest price to reach an airport with a certain
        # number of stops
        best = {}

        while heap:

            price, node, stops = heapq.heappop(heap)

            # Reached destination
            if node == dst:
                return price

            # Can't take more flights
            if stops > k:
                continue

            for nei, cost in adj[node]:

                new_price = price + cost
                new_stops = stops + 1

                # If this is a better way to reach the neighbor
                if (nei, new_stops) not in best or new_price < best[(nei, new_stops)]:

                    best[(nei, new_stops)] = new_price

                    heapq.heappush(
                        heap,
                        (new_price, nei, new_stops)
                    )

        return -1