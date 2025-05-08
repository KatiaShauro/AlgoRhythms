from copy import copy
from typing import List, Tuple, Dict

from src.vol1.tree_structure import Tree, Node
from src.abstractions.task import Task


class Task16_vol1(Task):
    def __init__(self, tr: Tree):
        self.max_way = tr.root.get_way_len()

    def find_max_way(self, node: Node, root: Node, stack : List):
        u = node
        way = u.get_way_len()
        if self.max_way <= way:
            stack.clear()
            root = u
            self.max_way = way

        stack.append(u)

        len_right = u.right.get_way_len() if u.right else 0
        len_left = u.left.get_way_len() if u.left else 0

        height_right = u.right.height if u.right else 0
        height_left = u.left.height if u.left else 0

        if (len_left <= len_right or height_left <= height_right) and u.right:
            next_node = u.right
            root_opposit = u.left
        else:
            next_node = u.left
            root_opposit = u.right

        if next_node is None:
            stack.reverse()
            return stack
        else:
            self.find_max_way(next_node, root, stack)
            if way == self.max_way:
                self.find_max_way(root_opposit, root, stack)
        return stack


    def execute(self):
        pass

    def get_info(self):
        pass


#tree = Tree([50, 20, 10, 5, 30, 60, 70, 65, 64, 63, 62, 61, 80, 90, 75, 100, 95, 97])
tree = Tree([50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40, 100, 120])
t = Task16_vol1(tree)
ar = t.find_max_way(tree.root, tree.root, [])
print(ar)