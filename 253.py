# Meeting Rooms

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        rooms = 0
        intervals.sort(key=lambda x: x[1])
        s = sorted(i[0] for i in intervals)
        e = sorted(i[1] for i in intervals)
        n = len(intervals)
        e_p = 0
        s_p = 0
        while s_p < n:
            if s[s_p] >= e[e_p]:
                rooms -= 1
                e_p += 1
            rooms += 1
            s_p += 1
        return rooms
  
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Min-heap to keep track of end times
        heap = []

        # Add the end time of the first meeting
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            # If the current meeting starts after or when the earliest meeting ends
            if intervals[i][0] >= heap[0]:
                # Reuse the room (remove the earliest ending meeting)
                heapq.heappop(heap)

            # Add the current meeting's end time to the heap
            heapq.heappush(heap, intervals[i][1])

        # The size of the heap is the number of conference rooms needed
        return len(heap)