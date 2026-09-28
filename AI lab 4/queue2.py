from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def popleft(self):
        if self.is_empty():
            return "Queue Underflow: Cannot popleft from empty queue"
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Your test code from the screenshot
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek()) # 10
print(q.popleft()) # 10
print(q.is_empty()) # False
print(q.size()) # 2