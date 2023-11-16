class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)
                
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop() 

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)