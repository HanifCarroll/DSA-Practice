class BinaryTree(object):
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        t = BinaryTree(value)
        if self.left_child is None:
            self.left_child = t
        else:
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, value):
        t = BinaryTree(value)
        if self.right_child is None:
            self.right_child = t
        else:
            t.right_child = self.right_child
            self.right_child = t

    def get_root(self):
        return self.key
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

def traverse_preorder(tree: BinaryTree):
    if tree is not None:
        print(tree.get_root())
        traverse_preorder(tree.get_left_child())
        traverse_preorder(tree.get_right_child())

def traverse_inorder(tree):
    if tree is not None:
        traverse_inorder(tree.get_left_child())
        print(tree.get_root())
        traverse_inorder(tree.get_right_child())

def traverse_postorder(tree):
    if tree is not None:
        traverse_postorder(tree.get_left_child())
        traverse_postorder(tree.get_right_child())
        print(tree.get_root())

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)

traverse_inorder(tree)