class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        output = [intervals[0][:]]
        out_index = 0
        end = intervals[0][1]
        
        for i, interval in enumerate(intervals[1:], start=1):
            start, end2 = interval
            if end < start:
                out_index += 1
                output.append(intervals[i][:])
            end = max(end, end2)
            output[out_index][1] = end
        return output

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)


## Did this on my own, knew I had to account for the [0,0] [0,0] edge case and sorting, figured out how to sort python via a tuple
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals or len(intervals) == 1:
        return intervals
    
    intervals.sort(key=lambda x: (x[0], x[1]))

    cur_first = intervals[0][0]
    cur_second = intervals[0][1]
    answer = []
    for i in range(1, len(intervals)):
        if cur_first <= intervals[i][1] and intervals[i][0] <= cur_second:
            # we know it is an overlap
            cur_first = min(cur_first, intervals[i][0])
            cur_second = max(cur_second, intervals[i][1])
        else:
            answer.append([cur_first, cur_second])
            cur_first = intervals[i][0]
            cur_second = intervals[i][1]
    answer.append([cur_first, cur_second])

    return  answer