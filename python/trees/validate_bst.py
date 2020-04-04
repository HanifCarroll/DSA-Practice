class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.val)
    
def is_valid_bst(root, minimum, maximum):
    if not root:
        return True
    if root.val <= minimum or root.val > maximum:
        return False
    return is_valid_bst(root.left, minimum, root.val) and is_valid_bst(root.right, root.val, maximum)
        


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n4.left = n2
n4.right = n6
n2.left = n1
n2.right = n3
n6.left = n5
n6.right = n7

def is_valid_bst_ref(node, a=None):
    if not node:
        return
    if a == None:
        a = []
    is_valid_bst_ref(node.left, a)
    a.append(node.val)
    is_valid_bst_ref(node.right, a)

    return a == sorted(a)

print(is_valid_bst(n4, float('-inf'), float('inf')))
print(is_valid_bst_ref(n4))