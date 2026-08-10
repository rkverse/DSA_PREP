class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first node")
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at the beginning")

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first node")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
        print(f"Inserted {data} at the end")

    # 3. Insert at a specific position
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        
        current.next = new_node
        print(f"Inserted {data} at position {position}")

    # 4. Delete a node by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        
        # If head node is to be deleted
        if current.data == value:
            self.head = current.next
            if self.head:
                self.head.prev = None
            print(f"Deleted {value}")
            return
        
        while current and current.data != value:
            current = current.next
        
        if current is None:
            print(f"{value} not found")
            return
        
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        
        print(f"Deleted {value}")

    # 5. Display forward
    def display_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        
        current = self.head
        print("Forward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # 6. Display backward
    def display_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        
        # Go to the last node
        current = self.head
        while current.next:
            current = current.next
        
        print("Backward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    # 7. Length
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ==================== TESTING ====================

dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
dll.insert_at_position(15, 2)

dll.display_forward()
# Output: 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None

dll.display_backward()
# Output: 30 <-> 20 <-> 15 <-> 10 <-> 5 <-> None

print("Length:", dll.length())

dll.delete_by_value(15)
dll.display_forward()