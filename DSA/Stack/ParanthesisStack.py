class Stack:  # Capital S (PEP8 convention)
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None  # Better to return None than string
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


# Solution for Valid Parentheses
def is_valid(s: str) -> bool:
    stack = Stack()
    mapping = {")": "(", "]": "[", "}": "{"}  # Clean matching
    
    for char in s:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if mapping[char] != top:   # Much cleaner check
                return False
    
    return stack.is_empty()


# Test
print(is_valid("{[()]}"))   # True
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))       # False
print(is_valid("([)]"))     # False
print(is_valid(""))         # True