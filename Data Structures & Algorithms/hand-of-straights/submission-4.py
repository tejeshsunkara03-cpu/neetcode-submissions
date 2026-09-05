from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            if count[first] == 0:
                heapq.heappop(min_heap)
                continue

            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1

        return True