import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        '''
        5 15, 10 15, 15 25, 16 27 is the edge case that we cant use the same logic as non-overlapping-intervals
        '''
        if not len(intervals):
            return 0
        rooms = []
        intervals.sort()
        heapq.heappush(rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)


    def optimal_chronological_order(self, intervals):
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        spointer = endpointer = rooms = 0      
            
        for spointer in range(len(intervals)):
            if start[spointer] >= end[endpointer]:
                rooms -= 1
                endpointer += 1
            rooms += 1
        return rooms

    def custom_chronological_order(self, intervals):
        start = [x[0] for x in intervals]
        end = [x[1] for x in intervals]
        start.sort()
        end.sort()
        spointer = 0
        endpointer = 0
        max_rooms = current_rooms = 0
        
        while spointer < len(intervals):
            if start[spointer] < end[endpointer]:
                current_rooms += 1
                max_rooms = max(max_rooms, current_rooms)
                spointer += 1
            else:
                current_rooms -= 1
                endpointer += 1
        return max_rooms

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)



li = [(12,11), (7,0), (3,13), (4,5)]
hi = heapq.heapify(li)
# print(li)