class MinStack:
    def __init__(self):
        self.items = []      # Main stack
        self.min_items = []  # Stack to keep track of minimums
    
    def push(self, item):
        self.items.append(item)
        
        # Push to min stack if it's the new minimum or equal
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        item = self.items.pop()
        # If the popped item is the current minimum, remove it from min stack
        if item == self.min_items[-1]:
            self.min_items.pop()
        return item
    
    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def get_min(self):
        if self.is_empty():
            return None
        return self.min_items[-1]
    
    def is_empty(self):
        return len(self.items) == 0


# Testing
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)

print("Top:", ms.top())           #  -3
print("Min:", ms.get_min())       #  -3

ms.pop()
print("Top after pop:", ms.top())      # 0
print("Min after pop:", ms.get_min())  # -2