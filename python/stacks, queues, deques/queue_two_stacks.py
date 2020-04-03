class Stack(object):
    def __init__(self):
        super().__init__()
        self.arr = []

    def push(self, x):
        self.arr.append(x)
    
    def pop(self):
        return self.arr.pop()
    
    def is_empty(self):
        return len(self.arr) == 0

class Queue2Stacks(object):
    def __init__(self):
        super().__init__()
        self.a = Stack()
        self.b = Stack()
    
    def enqueue(self, x):
        self.a.push(x)

    def dequeue(self):
        if self.a.is_empty() and self.b.is_empty():
            print('Both stacks are empty.')
        elif self.b.is_empty():
            self.swap()
        return self.b.pop()
    
    def swap(self):
        while not self.a.is_empty():
            self.b.push(self.a.pop())


q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print(q.dequeue())