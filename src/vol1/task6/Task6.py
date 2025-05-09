from copy import copy
from typing import List, Tuple, Dict

from src.vol1.tree_structure import Tree, Node
from src.abstractions.task import Task


class Task6_vol1(Task):
    def __init__(self):
        self.max_way = 0
        self.root = None

    def find_max_way(self, node: Node, stack : List) -> (List[Node], Node):
        u = node
        if not node:
            return [], None

        way = u.get_way_len()
        if self.max_way <= way and way != 2:
            stack.clear()
            self.root = u
            self.max_way = way

        stack.append(u)

        len_right = u.right.get_way_len() if u.right else 0
        len_left = u.left.get_way_len() if u.left else 0

        height_right = u.right.height if u.right else 0
        height_left = u.left.height if u.left else 0

        if len_left <= len_right and height_left <= height_right and u.right:
            next_node = u.right
            root_opposit = u.left
        else:
            next_node = u.left
            root_opposit = u.right

        if next_node is None:
            stack.reverse()
            return stack, self.root
        else:
            self.find_max_way(next_node, stack)
            if way == self.max_way and u in stack and u.key >= self.root.key:
                self.find_max_way(root_opposit, stack)
        return stack, self.root


    def first_part_of_solution(self, nodes : List[int]) -> (str, int, int):
        s = ''
        if not nodes:
            return s
        tree = Tree(nodes)
        self.max_way = tree.root.get_way_len()
        self.root = tree.root
        (arr, root) = self.find_max_way(tree.root, [])
        arr = list(reversed(arr)) if arr[-1].key < arr[0].key else arr.copy()
        length = len(arr)
        half = int(length/2)
        print(length)
        for a in arr:
            s += str(a.key) + ' '

        middle = arr[half] if length % 2 != 0 else (
            arr[half] if (
                    abs(root.key - arr[half].key) < abs(root.key - arr[half- 1].key)
            ) else arr[half - 1]
        )
        return s, root.key, middle.key


    def execute(self):
        pass


    def get_info(self):
        pass


# tree = Tree([50, 20, 10, 5, 30, 60, 70, 65, 64, 63, 62, 61, 80, 90, 75, 100, 95, 97])
# tree = Tree([50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40, 100, 120])
# tree = Tree([60, 50, 30, 20, 40, 10, 25, 35, 33])
#
print(Task6_vol1().first_part_of_solution([50, 20, 10, 30, 60]))