class stack:
    def __init__(self):
        self.items = []          # Internal list to store elements

    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        print("Popped", self.items[-1])
        return self.items.pop()
    

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        if len(self.items) == 0:
            return True
        return False

s = stack()
sample="{[(}]}"
for char in sample:
    if char in "{[(":
        s.push(char)
    elif char in "}])":
        if s.is_empty():
            print("Unbalanced")
            break
        top = s.pop()
        if (char == "}" and top != "{") or (char == "]" and top != "[") or (char == ")" and top != "("):
            print("Unbalanced")
            break
else:
    if s.is_empty():
        print("Balanced")
    else:
        print("Unbalanced")