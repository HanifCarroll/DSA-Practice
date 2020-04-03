class TreeNode(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return self.value

    def add_left_child(self, value):
        self.left = TreeNode(value, self)
        return self.left

    def add_right_child(self, value):
        self.right = TreeNode(value, self)
        return self.right

    def visit(self):
        print(self.value)


class BinaryTree(object):
    def __init__(self, value):
        self.root = TreeNode(value, None)

    def _preorder(self, node):
        if node:
            node.visit()
            self._preorder(node.left)
            self._preorder(node.right)

    def _inorder(self, node):
        if node:
            self._preorder(node.left)
            node.visit()
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._preorder(node.left)
            self._preorder(node.right)
            node.visit()

    def _levelorder(self, node):
        q = []
        q.append(node)
        while len(q):
            current = q.pop(0)
            if current:
                current.visit()
                q.append(current.left)
                q.append(current.right)

    def _contains(self, value, node):
        if not node:
            return False
        else:
            if node.value == value:
                return node
            elif value < node.value:
                return self._contains(value, node.left)
            elif value > node.value:
                return self._contains(value, node.right)

    def _contains_iterative(self, value, node):
        current = node
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def _insert(self, value, node):
        if value == node.value:
            print('That item is already in the tree')
        elif value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = TreeNode(value, node)
        else:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = TreeNode(value, node)

    def _insert_iterative(self, value, node):
        current = node
        while current:
            if value == current.value:
                print('That item is already in the tree.')
                break
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(value, current)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(value, current)
                    break

    def preorder(self):
        self._preorder(self.root)

    def inorder(self):
        self._inorder(self.root)

    def postorder(self):
        self._postorder(self.root)

    def levelorder(self):
        self._levelorder(self.root)

    def contains(self, value):
        return self._contains(value, self.root)

    def insert(self, value):
        return self._insert_iterative(value, self.root)
    
    def delete(self, value):
        node = self.contains(value)
        if not node:
            print('Element not found')
            return
        elif not node.left and not node.right:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left and not node.right:
            node.value = node.left.value
            node.left = None
        elif node.right and not node.left:
            node.value = node.right.value
            node.right = None
        elif node.left and node.right:
            minimum = self.get_minimum(node.right)
            node.value = minimum.value
            minimum.parent.left = None
    
    def get_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# t = BinaryTree('A')
# t.root.add_left_child('B')
# t.root.add_right_child('C')
# t.root.left.add_left_child('D')
# t.root.left.add_right_child('E')
# t.root.right.add_left_child('F')
# t.root.right.add_right_child('G')

t = BinaryTree(8)
t.root.add_left_child(5)
t.root.add_right_child(10)
t.root.left.add_left_child(3)
t.root.left.add_right_child(6)
t.root.right.add_left_child(9)
t.root.right.add_right_child(12)

# print(t.contains(5))
t.insert(2)
t.insert(4)
t.insert(11)
t.insert(13)
t.delete(10)
t.levelorder()
