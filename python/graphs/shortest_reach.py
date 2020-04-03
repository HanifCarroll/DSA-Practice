from typing import List

class Node(object):
    def __init__(self, id: int):
        self.id = id
        self.children: List['Node'] = []
    
    def __repr__(self):
        return str(self.id)
    
    def add_child(self, child: 'Node'):
        self.children.append(child)
    
    def add_children(self, *children):
        self.children.extend([*children])
    


def shortest_reach(node: Node) -> List[int]:
    edge_length = 6
    distances = [-1] * 7
    distances[0] = 0
    distances[node.id] = 0
    stack = []
    stack.append(node)
    while len(stack):
        node = stack.pop()
        for child in node.children:
            if distances[child.id] == -1:
                distances[child.id] = distances[node.id] + edge_length
                stack.append(child)
    return distances

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.add_child(b)
b.add_children(c, d)
d.add_children(e, f)
print(shortest_reach(a))