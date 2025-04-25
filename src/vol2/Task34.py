from typing import List, Tuple, Dict
from src.abstractions.task import Task


class Task34_vol2(Task):
    def dp_solution(self, arr: List[Tuple[int, int]]) -> Tuple[int, int]:
        delta = []
        d = 0
        for t in arr:
            a, b = t
            delta.append(a - b)
            d += (a - b)
        dp = {}
        dp[d] = 0
        min_d = d
        for i in delta:
            diff = -2 * i
            new_entries = {}
            for d, value in dp.items():
                d_new = d + diff
                new_entries[d_new] = min(dp.get(d_new, float('inf')),
                                         value + 1)
                if abs(d_new) < abs(min_d):
                    min_d = d_new
            dp.update(new_entries)
            print(dp)

        v1 = dp.get(min_d, float('inf'))
        v2 = dp.get(-min_d, float('inf'))

        if v1 < v2:
            return v1, abs(min_d)
        else:
            return v2, abs(-min_d)

    def execute(self, arr: List[Tuple[int, int]]) -> Tuple[int, int]:
        return self.dp_solution(arr)
    
    def get_info(self) -> Dict[str, str]:
        cond = ("Доминошка – это прямоугольная плитка, лицевая сторона которой разделена на два квадрата,"
        + "каждый из которых содержит от 0 до 6 точек. Пример: \n"
        + "6   1   1   1\n"
        + "-   -   -   -\n"
        + "1   5   3   2 \n"
        + "Количество точек в верхней строке равно 6 + 1 + 1 + 1 = 9 и количество в нижней 1 + 5 + 3 + 2 = 11. "
        + "Разница между нижней и верхней строкой равна |11 - 9| = 2. "
        + "Разница – это абсолютное значение разности двух сумм. Каждую доминошку можно перевернуть на"
        + " 180 градусов, меняя местами верхний и нижний квадраты."
        + "Необходимо определить, какое минимальное количество поворотов следует сделать для минимизации разности? "
        + "В приведенном примере нужно повернуть последнюю доминошку для того, чтобы уменьшить разницу до нуля. В этом случае ответом будет 1.")
        return {
            "title": "Доминошки",
            "condition": cond,
            "input": "Список кортежей (a, b), где a и b — целые числа, верхняя и нижняя сторона домино соответственно.",
            "output": "Кортеж из двух целых: (минимальное количество изменений, минимальное отклонение)."
        }

    def greedy_solution(self, arr: List[Tuple[int, int]]) -> Tuple[int, int]:
        delta = []
        d = 0
        for t in arr:
            a, b = t
            delta.append(a - b)
            d += (a - b)
        count = 0
        for item in delta:
            if abs(d + (-item) * 2) < abs(d):
                d += (-item) * 2
                count += 1
        return (count, abs(d))

    # 2^n
    def calc_diff_commented(self, arr, count, d, depth=0):
        indent = "  " * depth

        print(f"{indent}-> calc_diff(arr={arr}, count={count}, d={d})")

        if len(arr) == 0:
            print(f"{indent}<- Базовый случай: (count={count}, d={d})")
            return (count, d)

        print(f"{indent}Без вращения:")
        without_rotate = self.calc_diff(arr[1:], count, d, depth + 1)

        print(f"{indent}С вращением (+1 к count, d += {-2 * arr[0]}):")
        rotate = self.calc_diff(arr[1:], count + 1, d + (-arr[0] * 2),
                                depth + 1)

        if abs(rotate[1]) < abs(without_rotate[1]):
            print(
                f"{indent}Выбрано вращение: (count={rotate[0]}, d={rotate[1]})"
                )
            return rotate
        else:
            print(f"{indent}Выбрано без вращения: (count={without_rotate[0]},"
                  f"d={without_rotate[1]})")
            return without_rotate

    # 2^n
    def calc_diff(self, arr, count, d):
        if len(arr) == 0:
            return (count, d)
        without_rotate = self.calc_diff(arr[1:], count, d)
        rotate = self.calc_diff(arr[1:], count + 1, d + (-arr[0] * 2))
        if abs(rotate[1]) < abs(without_rotate[1]):
            return rotate
        else:
            return without_rotate

    def brute_force_solution(self,
                             arr: List[Tuple[int, int]]) -> Tuple[int, int]:
        delta = []
        d = 0
        for t in arr:
            a, b = t
            delta.append(a - b)
            d += (a - b)
        result = self.calc_diff(delta, 0, d)
        return result


if __name__ == "__main__":
    task = Task34_vol2()
    lst = [(3, 5), (2, 4), (1, 6)]
    ans = task.dp_solution(lst)
    print("dp:")
    print(f'Количество перестановок: {ans[0]}, минимальная разность: {ans[1]}')
    ans = task.greedy_solution(lst)
    print("greedy:")
    print(f'Количество перестановок: {ans[0]}, минимальная разность: {ans[1]}')
    ans = task.brute_force_solution(lst)
    print("brute force:")
    print(f'Количество перестановок: {ans[0]}, минимальная разность: {ans[1]}')
