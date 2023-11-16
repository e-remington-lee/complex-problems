class Solution:
    def insert(self, intervals, newInterval):
        start2, end2 = newInterval
        response = []
        index = 0
        while index < len(intervals) and start2 > intervals[index][0]:
            response.append(intervals[index][:])
            index += 1
        
        if not response or response[index - 1][1] < start2:
            response.append(newInterval)
        else:
            response[-1][1] = max(response[-1][1], end2)
        
        for i in range(index, len(intervals)):
            if response[-1][1] >= intervals[i][0]:
                response[-1][1] = max(response[-1][1], intervals[i][1])  
            else:
                response.append(intervals[i][:])

        return response

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
