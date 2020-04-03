class MinHeap(object):
    def __init__(self):
        self.items = []
        self.size = 0
    
    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size 

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size 

    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_right_child_index(self, index):
        return (index * 2) + 2
    
    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def insert(self, val):
        self.items.append(val)
        self.size += 1
        self.heapify_up()
    
    def extract(self):
        item = self.items[0]
        self.size -= 1
        self.swap(0, self.size)
        self.items.pop()
        self.heapify_down()
        return item
    
    def heapify_up(self):
        item_index = self.size - 1
        item = self.items[item_index]
        while self.has_parent(item_index) and self.parent(item_index) > item:
            parent_index = self.get_parent_index(item_index)
            self.swap(item_index, parent_index)
            item_index = parent_index
            item = self.items[item_index]
        
    def heapify_down(self):
        item_index = 0
        item = self.items[item_index]
        while self.has_left_child(item_index):
            lesser_child_index = self.get_left_child_index(item_index)
            if self.has_right_child(item_index) and self.right_child(item_index) < self.items[lesser_child_index]:
                lesser_child_index = self.get_right_child_index(item_index)
            
            if item < self.items[lesser_child_index]:
                break
            else:
                self.swap(item_index, lesser_child_index)
                item = self.items[lesser_child_index]
                item_index = lesser_child_index
    
    
heap = MinHeap()
heap.insert(6)
heap.insert(7)
heap.insert(10)
heap.insert(12)
heap.insert(14)
heap.insert(17)
heap.insert(2)

print(heap.extract())
print(heap.extract())