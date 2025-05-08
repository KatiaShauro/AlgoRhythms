from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    key: int
    value: str
    height: int = 0
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __str__(self):
        return (f"k: {self.key}, v: {self.value}, h: {self.height}, "
                f"left: {self.left is not None}, right: {self.right is not None}")

    def swap_nodes(self, other: 'Node') -> None:
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value


    @staticmethod
    def get_height(node: 'Node'):
        if node:
            return node.height
        else: return -1


    @staticmethod
    def update_height(node: 'Node'):
        node.height = max(Node.get_height(node.right), Node.get_height(node.left)) + 1


    @staticmethod
    def insert(key: int, val: str, node: 'Node'):
        if not node:
            return Node(key, val)
        if key == node.key:
            raise ValueError("Keys must be unique! ", key)
        elif node.key > key:
            node.left = Node.insert(key, val, node.left)
        elif node.key < key:
            node.right = Node.insert(key, val, node.right)

        Node.update_height(node)
        return node


    @staticmethod
    def print_tree(node: 'Node'):
        if node is None:
            return
        print(f"{node.key}  {node.value};")
        Node.print_tree(node.left)
        Node.print_tree(node.right)


    @staticmethod
    def find_node(key: int, node: 'Node'):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key > key:
            return Node.find_node(key, node.left)
        elif node.key < key:
            return Node.find_node(key, node.right)


    @staticmethod
    def find_maximum(node: 'Node'):
        if node.right is None:
            return node
        return Node.find_maximum(node.right)


    @staticmethod
    def find_minimum(node: 'Node'):
        if node.left is None:
            return node
        return Node.find_minimum(node.left)


    @staticmethod
    def delete_node(key: int, node: 'Node'):
        if not node:
            raise ValueError('No node with such key')
        if node.key > key:
            node.left = Node.delete_node(key, node.left)
        elif node.key < key:
            node.right = Node.delete_node(key, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left and node.right:
                temp = Node.find_minimum(node.right)
                temp.swap_nodes(node)
                node.right = Node.delete_node(temp.key, node.right)
            elif node.left is None:
                return node.right
            else:
                return node.left
        Node.update_height(node)
        return node


    @staticmethod
    def tree_to_list(node: 'Node'):
        if node is None:
            return []
        result = []
        if node.left or node.right:
            lr = ''
            if node.left:
                lr += 'L'
            if node.right:
                lr += 'R'
            result.append((node.key, lr, node.height))
        else:
            result.append((node.key, '|', node.height))

        result += Node.tree_to_list(node.left)
        result += Node.tree_to_list(node.right)
        return result


    def get_way_len(self):
        index = 0
        if self.left:
            index += 1
            index += self.left.height
        if self.right:
            index += 1
            index += self.right.height
        return index


    def __repr__(self):
        return f"(key = {self.key}, h = {self.height})"
