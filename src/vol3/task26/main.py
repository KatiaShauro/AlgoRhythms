from BlackBox import BlackBox
from src.vol3.task26.BlackBoxTreap import BlackBoxTreap
from typing import List


def print_treap_elements(root, elements=None):
    if elements is None:
        elements = []
    if root:
        print_treap_elements(root.left, elements)
        elements.append(root.value)
        print_treap_elements(root.right, elements)
    return elements

def main():
    bb = BlackBox()

    coms = [
        ("Add", 3),
        ("Get", ),
        ("Add", 10),
        ("Add", -3),
        ("Add", 0),
        ("Get",),
        ("Add", 20),
        ("Get",),
        ("Get", ),
        ("Add", 14),
        ("Add", -10),
        ("Add", 1),
        ("Get",),
        ("Add", -20),
    ]

    for c in coms:
        if c[0] == "Add":
            bb.add(int(c[1]))
            print(f"Add({c[1]}): i={bb.i}, BlackBox={sorted([-x for x in bb.max_heap] + bb.min_heap)}")
        else:
            #Костыль
            print(f"Get(): i={bb.i + 1}, Result={bb.get()}")

def main_treap():
    bb = BlackBoxTreap()

    coms = [
        ("Add", 3),
        ("Get", ),
        ("Add", 10),
        ("Add", -3),
        ("Add", 0),
        ("Get",),
        ("Add", 20),
        ("Get",),
        ("Get", ),
        ("Add", 14),
        ("Add", -10),
        ("Add", 1),
        ("Get",),
        ("Add", -20),
    ]

    for _ in coms:
        if _[0] == "Add":
            bb.add(_[1])
            elements = list(print_treap_elements(bb.root))
            print(f"Add({_[1]}): i={bb.i}, BlackBox={sorted(elements)}")
        else:
            result = bb.get()
            elements = print_treap_elements(bb.root)
            print(f"Get(): i={bb.i}, Result={result}, BlackBox={sorted(elements)}")


def execute(coms : List):
    bb = BlackBox()
    for c in coms:
        if c[0] == "Add":
            bb.add(int(c[1]))
            print(f"Add({c[1]}): i={bb.i}, BlackBox={sorted([-x for x in bb.max_heap] + bb.min_heap)}")
        else:
            print(f"Get(): i={bb.i + 1}, Result={bb.get()}")


if __name__ == '__main__':
    #main()
    main_treap()
    # execute([
    #     ("Add", 3),
    #     ("Get", ),
    #     ("Add", 10),
    #     ("Add", -3),
    #     ("Add", 0),
    #     ("Get",),
    #     ("Add", 20),
    #     ("Get",),
    #     ("Get", ),
    #     ("Add", 14),
    #     ("Add", -10),
    #     ("Add", 1),
    #     ("Get",),
    #     ("Add", -20),
    # ])
