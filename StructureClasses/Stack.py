# here we are creating a new Python class which represents a stack data structure
class Stack:
    def __init__(self, initialStack : list = []):
        self.stack = initialStack
    
    def push(self, item : str) -> list:
        self.stack.append(item)
    
    def pop(self):
        temp = self.stack[:-1]
        self.stack = temp
    
    def peek(self) -> str:
        return self.stack[-1]
    
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False 
    
    def search(self, item : str) -> int:
        for i in range(len(self.stack)):
            if self.stack[i] == item:
                return i
        return -1