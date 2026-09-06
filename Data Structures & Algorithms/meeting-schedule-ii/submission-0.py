import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = []

        heapq.heappush(rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, intervals[i].end)

        return len(rooms)