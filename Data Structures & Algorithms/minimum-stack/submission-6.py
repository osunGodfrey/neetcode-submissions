class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_stack_index = -1
        self.top_min_stack_index = -1
        
        

    def push(self, val: int) -> None:
        self.stack = self.stack + [val]
        self.top_stack_index += 1
        # print(self.stack)
        if self.top_min_stack_index == -1:
            self.min_stack = self.min_stack + [val]
            self.top_min_stack_index += 1
        elif val <= self.min_stack[self.top_min_stack_index]:
            self.min_stack = self.min_stack + [val]
            self.top_min_stack_index += 1
        else:
            return None

    def pop(self) -> None:
        if self.top_min_stack_index == -1:
            return None
        elif self.min_stack[self.top_min_stack_index] == self.stack[self.top_stack_index]:
            self.min_stack.pop()
            self.top_min_stack_index -= 1
        if self.top_stack_index == -1:
            return None
        else:
            self.stack.pop()
            self.top_stack_index -= 1

        
    def top(self) -> int:
        if self.top_stack_index == -1:
            return -1
        else:
            return self.stack[self.top_stack_index]
        

    def getMin(self) -> int:
        if self.top_min_stack_index == -1:
            return -1
        else:
            return self.min_stack[self.top_min_stack_index]
        
