from src.vol2.Task34 import Task34_vol2
from src.vol3.task25.CubeProblemGenerator import CubeProblemGenerator
from src.vol3.task25.CubePathFinder import CubePathFinder
from src.vol3.task25.CubeProblemVisualizer import CubeProblemVisualizer
from typing import Dict, List, Tuple


class Task25_vol3:
    def main(self):
        while True:
            problem = CubeProblemGenerator.generate_problem(
                min_size=7,
                max_size=10,
                min_val=1,
                max_val=9
            )

            CubeProblemVisualizer.display_problem(problem)

            print("\nВычисление оптимального пути...")
            finder = CubePathFinder(problem.grid, problem.face_values)
            total_penalty, optimal_path = finder.find_optimal_path(problem.start_pos, problem.end_pos)

            CubeProblemVisualizer.display_solution(optimal_path, total_penalty)

            try:
                start_another_time = int(input("\nЖелаете продолжить программу?(1/0)"))
                if start_another_time:
                    continue
                break
            except ValueError:
                print("Некорректные вводимые данные.")

    def execute(self, min_size: int, max_size: int, min_val: int, max_val: int) -> int:
        problem = CubeProblemGenerator.generate_problem(
            min_size = int(min_size),
            max_size = int(max_size),
            min_val = int(min_val),
            max_val = int(max_val),
        )

        finder = CubePathFinder(problem.grid, problem.face_values)
        total_penalty, optimal_path = finder.find_optimal_path(problem.grid, problem.face_values)
        return total_penalty

    def get_info(self) -> Dict[str, str]:
        cond = ('Задано поле A размера m × n, разбитое на квадраты единичной длины. '
                'Каждому квадрату поля с координатами [i,j] ставится в соответствии некоторое '
                'положительное число A[i,j] (т. е. задана матрица целых положительных чисел). '
                'Есть кубик с шестью гранями (грань кубика – это квадрат единичной длины). '
                'На i-й грани кубика написано некоторое число s[i] > 0 (i=1..6). Если в некоторый'
                'момент времени кубик лежит гранью k на единичном квадрате с координатами [i,j],'
                ' то за прохождение кубиком этого поля взимается штраф |A[i,j]-s[k]|. Кубик '
                'перемещается по полю, переворачиваясь с одной грани на любую другую из четырех '
                'соседних, и за один такой поворот оказывается на соседнем единичном квадрате поля.'
                'Необходимо определить, какой гранью (и какой ориентацией) должен лежать кубик в '
                'позиции поля с координатами (x1, y1), чтобы суммарный штраф, который нужно заплатить'
                ' за перекатывание кубика в позицию поля с координатами (x2, y2), был минимален.')
        return {
            "title": "Кубик",
            "condition": cond,
            "input": "min_size : int, max_size : int, min_val : int, max_val : int",
            "output": "total_penalty : int",
        }

    def BFS_algo(self):
        while True:
            problem = CubeProblemGenerator.generate_problem(
                min_size=7,
                max_size=10,
                min_val=1,
                max_val=1
            )

            CubeProblemVisualizer.display_problem(problem)

            print("\nВычисление оптимального пути...")
            finder = CubePathFinder(problem.grid, [1, 2, 3, 4, 5, 6])
            total_penalty, optimal_path = finder.bfs_find_optimal_path(problem.start_pos, problem.end_pos)

            CubeProblemVisualizer.display_solution(optimal_path, total_penalty)

            try:
                start_another_time = int(input("\nЖелаете продолжить программу?(1/0)"))
                if start_another_time:
                    continue
                break
            except ValueError:
                print("Некорректные вводимые данные.")

if __name__ == "__main__":
    #Task25_vol3().main()
    #Task25_vol3().execute()
    Task25_vol3().BFS_algo()

