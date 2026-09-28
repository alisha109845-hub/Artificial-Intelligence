class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack: ", self.items)

stack= Stack()

stack.push(10)
stack.push(20)
stack.push(30)
# different data types
stack.push("Hello")
stack.push('A')
stack.push((1, 2, 3))
stack.push({"name": "Ali"})

print(stack.peek())
print(stack.pop())
print(stack.is_empty())
print(stack.size())
stack.display()


    