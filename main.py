# class Node(object):
#     def __init__(self, value, next=None):
#         self.value=value
#         self.next=next

class Node(object):
    def __init__(self, value, right=None, left=None):
        self.value=value
        self.right=right
        self.left=left
 
from collections import defaultdict
class Solution:
    def answer(self, courses):
        response=[]
        recent_seen=defaultdict(lambda: False)
        seen=defaultdict(lambda: False)
        for course in courses.keys():
            if not seen[course]:
                if self.answer_helper(course, courses, seen, recent_seen, ""):
                    return None
        return False

    def answer_helper(self, course, courses, seen, recent_seen, response):
        seen[course]=True
        recent_seen[course]=True
        for c2 in courses[course]:
            if not seen[c2]:
                if self.answer_helper(c2, courses, seen, recent_seen, course):
                    return True
            elif recent_seen[c2]:
                return True
            
        recent_seen[course]=False
        # response.append(course)
        return False
        
    # def answer(self, courses):
    #     response=[]
    #     seen=defaultdict(lambda: False)
    #     for course in courses.keys():
    #         recent_seen=defaultdict(lambda: False)
    #         if not seen[course]:
    #             if self.answer_helper(course, courses, seen, recent_seen, response):
    #                 return None
    #     return response

    # def answer_helper(self, course, courses, seen, recent_seen, response):
    #     seen[course]=True
    #     recent_seen[course]=True
    #     for c2 in courses[course]:
    #         if recent_seen[c2]:
    #             return True
    #         elif not seen[c2]:
    #             if self.answer_helper(c2, courses, seen, recent_seen, response):
    #                 return True
    #     recent_seen[course]=False
    #     response.append(course)
    #     return False 


def main():
    b = Node("b", left=Node("d"), right=Node("e"))
    c = Node("c", left=Node("f"), right=Node("g"))
    root = Node("a", left=b, right=c)
    x=Solution()
    courses = {
        'CSC300': ['CSC100', 'CSC200'], 
        'CSC200': ['CSC100'], 
        'CSC100': []
        }
    print(x.answer(courses))

    


if __name__=="__main__":
    main()


class NodesSumToZero(object):
    def answer(self, node):
        dummy_head=start = Node(0, node)
        map={}
        sum=0
        while start:
            sum+=start.value
            map[sum]=start
            start=start.next
        start=dummy_head
        sum=0
        while start:
            sum+=start.value
            start.next=map[sum].next
            start=start.next
        return dummy_head.next


# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)

