class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.size - 1

    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = data
        print(data, "inserted")

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        print("Removed:", removed)

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front Element:", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Driver Code
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

q.peek()