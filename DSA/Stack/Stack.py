class Stack:
    def __init__(self):
        self.items = []          # Internal list to store elements
    
    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return True
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return True
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        if len(self.items) == 0:
            return True
        return False
    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)
    
    def __str__(self):
        """For nice printing"""
        return str(self.items)

s = Stack()

s.push(10)
print("Pushed",s.peek())
s.push(20)
print("Pushed",s.peek())
s.push(30)
print("Pushed",s.peek())
s.push(40)
print("Pushed",s.peek())
s.push(50)
print("Pushed",s.peek())

print("Stack:", s)           # [10, 20, 30, 40, 50]
print("Top element:", s.peek())   # 50
print("Popped:", s.pop())         # 50
print("Stack after pop:", s)       # [10, 20, 30, 40]
print("Size:", s.size())          # 4
print("Is empty?", s.is_empty())  # False