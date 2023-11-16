class Solution:
    def canAttendMeetings(self, intervals):
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x[1])
        
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                return False
            end = intervals[i][1]
        return True

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)