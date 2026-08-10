class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        print(f"Inserted {data} at the end")

    # 3. Insert at a specific position (0-based index)
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        
        new_node = Node(data)
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}")

    # 4. Delete a node by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        # If head node is to be deleted
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value}")
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next is None:
            print(f"{value} not found")
            return
        
        current.next = current.next.next
        print(f"Deleted {value}")

    # 5. Search for a value
    def search(self, value):
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                print(f"{value} found at position {position}")
                return True
            current = current.next
            position += 1
        
        print(f"{value} not found")
        return False

    # 6. Get the length of the list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 7. Display the linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 8. Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        print("Linked List reversed")


# ==================== TESTING ====================

ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.insert_at_position(15, 2)

ll.display()
# Output: 5 -> 10 -> 15 -> 20 -> 30 -> None

print("Length:", ll.length())       # 5

ll.search(15)                       # Found at position 2
ll.delete_by_value(15)
ll.display()

ll.reverse()
ll.display()