from vol1.tree_structure import Node

class Tree:
    root : Node = None
    quantity: int = 0
    height: int = -1

    def __init__(self, numbers : list):
        for num in numbers:
            if type(num) is not int or num <= 0:
                print(f"Incorrect list format: {num}")
            else:
                self.insert(num, "value")


    def insert(self, key: int, value: str = "value"):
        self.root = Node.insert(key, value, self.root)
        self.quantity += 1
        self.height = self.root.height


    def print_tree(self):
        Node.print_tree(self.root)


    def find_node(self, key: int):
        node = Node.find_node(key, self.root)
        if node is None:
            print("No node with such key")
        else:
            print("Node is here: ", node)
            return node


    def find_maximum(self):
        node = Node.find_maximum(self.root)
        print("Maximum: ", node)


    def find_minimum(self):
        node = Node.find_minimum(self.root)
        print("Minimum: ", node)


    def init_from_input(self):
        print("Enter nums for tree...\nIf you want to finish - press 0")
        num = 1
        nums = list()
        while num:
            try:
                num = int(input())
            except ValueError:
                print("Number mast be integer")
                continue
            if num < 0:
                print("Number mast be positive")
                continue
            elif num != 0:
                nums.append(num)

        for num in nums:
            self.insert(num, "value")


    def delete_node(self, key: int):
        self.root = Node.delete_node(key, self.root)
        self.quantity -= 1


    def tree_to_str(self):
        pr = Node.tree_to_list(self.root)
        print(pr)

