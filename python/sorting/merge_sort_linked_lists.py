class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def print(self):
        if not self.head:
            print('Empty')
        else:
            nodes = []
            current = self.head
            while current:
                nodes.append(current)
                current = current.next
            print(nodes)
    
    def insert(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def merge_sort(self):
        return self._merge_sort(self.head)
    
    def _merge_sort(self, a):
        if not a or not a.next:
            return a

        middle = self.find_middle(a)
        b = middle.next
        middle.next = None

        left = self._merge_sort(a)
        right = self._merge_sort(b)
        print(a, b)

        return self.sorted_merge(left, right)

    
    def find_middle(self, a):
        if not a:
            print('No middle to find')
            return a
        else:
            slow = fast = a
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.val <= b.val:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result


l = LinkedList()
l.insert(5)
l.insert(3)
l.insert(7)
l.insert(2)
l.insert(8)
l.insert(1)

l.print()
l.merge_sort()
l.print()