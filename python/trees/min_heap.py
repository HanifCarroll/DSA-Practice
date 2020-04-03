class MinHeap(object):
    def __init__(self):
        self.items = []
        self.size = 0
    
    def __repr__(self):
        return str(self.items)

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return index >= 0

    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_right_child_index(self, index):
        return (index * 2) + 2

    def get_parent_index(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, a, b):
        self.items[a], self.items[b] = self.items[b], self.items[a]

    def peek(self):
        return self.items[0]

    def insert(self, value):
        self.items.append(value)
        self.size += 1
        self.heapify_up()

    def extract(self):
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        self.heapify_down()
        return item

    def heapify_up(self):
        current_index = self.size - 1
        while self.has_parent(current_index) and self.parent(current_index) > self.items[current_index]:
            parent_index = self.get_parent_index(current_index)
            self.swap(current_index, parent_index)
            current_index = parent_index

    def heapify_down(self):
        current_index = 0
        while self.has_left_child(current_index):
            smaller_child_index = self.get_left_child_index(current_index)
            if (self.has_right_child(current_index) and
                    self.right_child(current_index) < self.left_child(current_index)):
                smaller_child_index = self.get_right_child_index(current_index)
            if self.items[current_index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(current_index, smaller_child_index)
                current_index = smaller_child_index

heap = MinHeap()
heap.insert(5)
heap.insert(2)
heap.insert(13)
heap.insert(3)
heap.insert(17)
heap.insert(6)
heap.insert(14)
heap.insert(8)
heap.insert(9)
heap.insert(10)
print(heap.extract())
print(heap.extract())
print(heap)