from src.vol1.tree_structure import Tree

if __name__ == "__main__":
    tree = Tree()
    tree1 = Tree()

    # tree.insert(40)
    # tree.insert(30)
    # tree.insert(35)
    # tree.insert(20)
    # tree.insert(22)
    # tree.insert(21)
    # tree.insert(25)
    # tree.insert(50)
    # tree.insert(60)
    # tree.insert(55)
    # tree.insert(80)

    # tree.insert(40)
    # tree.insert(30)
    # tree.insert(35)
    # tree.insert(32)
    # tree.insert(20)
    # tree.insert(52)
    # tree.insert(60)

    tree.insert(80)
    tree.insert(50)
    tree.insert(40)
    tree.insert(60)
    tree.insert(100)
    tree.insert(90)
    tree.insert(110)


    tree.tree_to_str()
    tree1.init_from_input()

    print(Tree.compare_trees(tree, tree1))
