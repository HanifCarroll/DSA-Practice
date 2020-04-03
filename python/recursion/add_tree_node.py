class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

    def add(self, value):
        if value > self.value:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.add(value)
        elif value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            print('That value is in the tree')
    
    def print_level_order(self):
        q = []
        q.append(self)
        while len(q):
            current = q.pop()
            if current:
                print(current)
                q.append(current.left)
                q.append(current.right)

a = Node(1)
a.add(3)
a.add(4)
a.add(2)
a.print_level_order()
