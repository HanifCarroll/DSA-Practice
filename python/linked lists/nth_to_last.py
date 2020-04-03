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

def nth_to_last(node, delay):
    count = 0
    slow = node
    fast = node
    while fast.next:
        if count < delay:
            count += 1
            fast = fast.next
        else:
            fast = fast.next
            slow = slow.next
    return slow

print(nth_to_last(a, 2))