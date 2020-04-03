# ['A', [], []]

def binary_tree(value):
    return [value, [], []]

def insert_left(root, new_branch):
    temp = root.pop(1)
    if len(temp) > 1:
        root.insert(1, [new_branch, temp, []])
    else:
        root.insert(1, [temp, [], []])

def insert_right(root, new_branch):
    temp = root.pop(2)
    if len(temp) > 1:
        root.insert(2, [new_branch, [], temp])
    else:
        root.insert(2, [temp, [], []])


def get_root(root):
    return root[0]

def get_left(root):
    return root[1]

def get_right(root):
    return root[2]

tree = binary_tree('A')
print(tree)