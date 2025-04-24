from src.vol1.tree_structure import Tree

if __name__ == "__main__":
    tree1 = Tree([80, 50, 40, 60, 100, 90, 110])
    tree2 = Tree([80, 50, 40, 60, 100, 90, 110])

    print(Tree.compare_trees(tree2, tree1))
