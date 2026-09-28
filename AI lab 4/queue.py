class Queue:

    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def display(self):
            print("Queue: ", self.items)

q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())
print(q.dequeue())
print(q.is_empty())
print(q.size())

q.display()

    