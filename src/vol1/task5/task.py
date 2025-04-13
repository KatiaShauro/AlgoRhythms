from src.vol1.tree_structure import Tree

if __name__ == "__main__":
    tree = Tree()

    # tree.insert(5)
    # tree.insert(3)
    # tree.insert(7)
    # tree.insert(2)
    # tree.insert(4)

    tree.init_from_input()

    tree.print_tree()
    tree.find_node(56)
    tree.find_node(1)

    tree.find_maximum()
    tree.find_minimum()

    tree.delete_node(1)
    tree.print_tree()
    tree.find_node(50)
    tree.find_node(77)