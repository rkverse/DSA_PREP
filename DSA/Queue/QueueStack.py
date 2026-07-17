class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0


class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = Stack()   # For enqueue
        self.stack2 = Stack()   # For dequeue
    
    def enqueue(self, item):
        """Add item to the queue (O(1))"""
        self.stack1.push(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """Remove and return front item (Amortized O(1))"""
        if self.stack2.is_empty():
            # Transfer all elements from stack1 to stack2
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        if self.stack2.is_empty():
            return None
        return self.stack2.pop()
    
    def front(self):
        """Return front item without removing"""
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        if self.stack2.is_empty():
            return None
        return self.stack2.peek()
    
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
    
    def size(self):
        # Not efficient, but for understanding
        return len(self.stack1.items) + len(self.stack2.items)


# Testing
q = QueueUsingTwoStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())      # 10
print("Dequeued:", q.dequeue()) # 10
print("Dequeued:", q.dequeue()) # 20
q.enqueue(40)
print("Front:", q.front())      # 30
print("Dequeued:", q.dequeue()) # 30