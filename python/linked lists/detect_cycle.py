class Node(object):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

def detect_cycle(node):
    seen = []
    while node:
        if node in seen:
            return True
        else:
            seen.append(node)
            node = node.next
    return False

def detect_cycle2(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

print(detect_cycle2(a))

d.next = a
print(detect_cycle2(a))