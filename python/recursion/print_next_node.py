class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

def print_list_reversed(node):
    if node and node.next:
        print_list(node.next)
        print(node.value)
    if not node.next:
        print('End of the chain!')
        return

def print_list(node):
    print(node)
    if node.next:
        print_list(node.next)

def reverse_list(node):
    current = node
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

# reverse_list(a)
# print_list(g)
print(chr(78))