import random

class TreapNode:
    def __init__(self, value):
        self.value = value
        self.priority = random.randint(0, 10**18)
        self.size = 1
        self.left = None
        self.right = None

    def update_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


def split(node, key):
    if node is None:
        return (None, None)
    if node.value <= key:
        left, right = split(node.right, key)
        node.right = left
        node.update_size()
        return (node, right)
    else:
        left, right = split(node.left, key)
        node.left = right
        node.update_size()
        return (left, node)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        left.update_size()
        return left
    else:
        right.left = merge(left, right.left)
        right.update_size()
        return right

def insert(root, value):
    left, right = split(root, value)
    new_node = TreapNode(value)
    return merge(merge(left, new_node), right)

def find_kth(node, k):
    if node is None:
        return None
    left_size = node.left.size if node.left else 0
    if k == left_size + 1:
        return node.value
    elif k <= left_size:
        return find_kth(node.left, k)
    else:
        return find_kth(node.right, k - left_size - 1)


class BlackBoxTreap:
    def __init__(self):
        self.root = None
        self.i = 0

    def add(self, x):
        self.root = insert(self.root, x)

    def get(self):
        self.i += 1
        return find_kth(self.root, self.i)