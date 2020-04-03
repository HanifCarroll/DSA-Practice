class Stack(object):
    def __init__(self):
        self.arr = []

    def __repr__(self):
        return str(self.arr)

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr):
            return self.arr.pop()
        else:
            print('Can\'t pop an empty stack.')

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return self.arr == []

    def size(self):
        return len(self.arr)

stack = Stack()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)

stack.pop()
stack.pop()

print(stack)
print(stack.peek())
