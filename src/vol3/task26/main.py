from src.vol3.task26.BlackBox import BlackBox
from src.vol3.task26.BlackBoxTreap import BlackBoxTreap
from typing import List, Dict

class Task26_vol3:
    def print_treap_elements(self, root, elements=None):
        if elements is None:
            elements = []
        if root:
            Task26_vol3.print_treap_elements(self, root.left, elements)
            elements.append(root.value)
            Task26_vol3.print_treap_elements(self, root.right, elements)
        return elements

    def main(self):
        bb = BlackBox()

        coms = [
            ("Add", 3),
            ("Get",),
            ("Add", 10),
            ("Add", -3),
            ("Add", 0),
            ("Get",),
            ("Add", 20),
            ("Get",),
            ("Get",),
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
                # Костыль
                print(f"Get(): i={bb.i + 1}, Result={bb.get()}")

    def main_treap(self):
        bb = BlackBoxTreap()

        coms = [
            ("Add", 3),
            ("Get",),
            ("Add", 10),
            ("Add", -3),
            ("Add", 0),
            ("Get",),
            ("Add", 20),
            ("Get",),
            ("Get",),
            ("Add", 14),
            ("Add", -10),
            ("Add", 1),
            ("Get",),
            ("Add", -20),
        ]

        for _ in coms:
            if _[0] == "Add":
                bb.add(_[1])
                elements = list(Task26_vol3.print_treap_elements(bb.root))
                print(f"Add({_[1]}): i={bb.i}, BlackBox={sorted(elements)}")
            else:
                result = bb.get()
                elements = Task26_vol3.print_treap_elements(bb.root)
                print(f"Get(): i={bb.i}, Result={result}, BlackBox={sorted(elements)}")

    def execute(self, coms: List):
        bb = BlackBox()
        str = ""
        for c in coms:
            if c[0] == "Add":
                bb.add(int(c[1]))
                str += (f"Add({c[1]}): i={bb.i}, BlackBox={sorted([-x for x in bb.max_heap] + bb.min_heap)}")
            else:
                str += (f"Get(): i={bb.i + 1}, Result={bb.get()}")
        return str

    def get_info(self) -> Dict[str, str]:
        cond = ('Черный ящик организован наподобие примитивной базы данных. Он может хранить набор целых чисел и имеет'
                'выделенную переменную i. В начальный момент времени черный ящик пуст, а значение переменной i равно нулю.'
                'Черный ящик обрабатывает некоторую последовательность поступающих команд (запросов). Существует два'
                ' вида запросов:'
                '1) Add (x) – положить в черный ящик элемент x;'
                '2) Get – увеличить значение переменной i на 1 и выдать копию i-го минимального элемента черного ящика.'
                'Напомним, что i-м минимальным элементом последовательности называется число, которое стоит на i-м месте'
                ' в отсортированной по неубыванию последовательности.')
        return {
            "title": "Черный ящик",
            "condition": cond,
            "input": "Список кортежей (command, number), где command - Add или Get, number - число, над которым производится операция",
            "output": "Изменения в черном ящике."
        }


if __name__ == '__main__':
    #main()
    Task26_vol3.main_treap()
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
