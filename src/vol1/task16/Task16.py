from typing import List, Tuple, Dict

from src.vol1.tree_structure import Tree, Node
from src.abstractions.task import Task


class Task16_vol1(Task):
    def compare_trees(self, largest_tree: Tree, smallest_tree: Tree):
        large = Node.tree_to_list(largest_tree.root)
        small = Node.tree_to_list(smallest_tree.root)

        if abs(len(large) - len(small)) != 1:
            return "The number of nodes varies by more than one", None

        if len(large) < len(small):
            large, small = small, large

        is_modified = False
        candidate = None
        for index, node in enumerate(small):
            if large[index][1] == small[index][1]:
                continue
            elif is_modified and large[index + 1][1] == small[index][1]:
                continue
            elif (large[index][1] == 'LR' and (small[index][1] == 'L' or small[index][1] == 'R'))\
                or (large[index][1] == 'L' or large[index][1] == 'R' and small[index][1] == '|'):

                if is_modified:
                    return "Impossible", None
                is_modified = True

                if small[index][1] == 'L' or large[index][1] == 'L' or large[index][1] == 'R':
                    stick_counter = 0
                    i = index - 1
                    while i != -1:
                        if large[i][1] == 'LR' and stick_counter == 0:
                            break
                        if large[i][1] == '|': stick_counter += 1
                        if large[i][1] == 'LR': stick_counter -= 1
                        i -= 1
                    if i == -1:
                        candidate = large[len(large) - 1][0]
                    else:
                        candidate = large[i][0]
                else:
                    candidate = large[index][0]
                continue
            elif large[index][1] == '|' and small[index][1] != '|':
                if not is_modified:
                    return "Impossible", None
                continue
            return "Impossible", None
        return "Possible", candidate


    def execute(self, nodes1: List[int], nodes2 : List[int]) -> Tuple[str, int]:
        tree1 = Tree(nodes1)
        tree2 = Tree(nodes2)
        return self.compare_trees(tree1, tree2)


    def get_info(self) -> Dict[str, str]:
        cond = ("Заданы два дерева. Определить, можно ли одно дерево получить из второго (по структуре) "
                "в результате удаления некоторой вершины. Если можно, то указать ту из возможных для удаления вершин, "
                "которая имеет наибольший ключ (10 баллов). ")
        return {
            "title": "Сравнение структуры деревьев",
            "condition": cond,
            "input": "Два массива целых чисел - узлы сравниваемых деревьев",
            "output": "Кортеж из строки и целого: (Possible/Impossible, ключ_максимальной_вершины/None)."
        }


if __name__ == "__main__":
    task = Task16_vol1()
    large = [50, 20, 100, 10, 30, 25, 22, 33, 35]
    small = [50, 20, 100, 10, 30, 25, 22, 33]
    res = task.execute(large, small)
    print(res)
