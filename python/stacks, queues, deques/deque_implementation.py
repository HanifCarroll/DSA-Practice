class Deque(object):
    def __init__(self):
        super().__init__()
        self.arr = []
    
    def add_front(self, x):
        self.arr.insert(0, x)
    
    def remove_front(self):
        return self.arr.pop(0)

    def add_rear(self, x):
        self.arr.append(x)
    
    def remove_rear(self, x):
        return self.arr.pop()
