class Stack(object):
    def __init__(self):
        super().__init__()
        self.arr = []

    def pop(self):
        return self.arr.pop()

    def push(self, x):
        self.arr.append(x)
    
    def is_empty(self):
        return len(self.arr) == 0


class Node(object):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None
    
    def __repr__(self):
        return self.value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

print(a)

def reverse_list(node):
    s = Stack()
    current = node
    while current:
        s.push(current)
        current = current.next
    
    head = s.pop()
    current = head
    while not s.is_empty():
        node = s.pop()
        current.next = node
        current = node
    return head

def reverse_list2(node):
    current = node
    previous_node = None
    next_node = None

    while current:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
    return previous_node
    

print(reverse_list2(a))