import pandas as pd
from typing import List, Optional
from src.vol3.task25.CubeProblem import CubeProblem


class CubeProblemVisualizer:
    @staticmethod
    def display_problem(problem: CubeProblem):
        print("\n" + "=" * 40)
        print("Параметры задачи о кубике:")
        print("=" * 40)

        print("\nПоле:")
        print(pd.DataFrame(problem.grid).to_string(index=False, header=False))

        print("\nЗначения на гранях кубика:")
        faces = ["Верх", "Низ", "Перед", "Зад", "Лево", "Право"]
        for face, value in zip(faces, problem.face_values):
            print(f"{face}: {value}")

        print(f"\nНачальная позиция: {problem.start_pos}")
        print(f"Конечная позиция: {problem.end_pos}")

    @staticmethod
    def display_solution(optimal_path: List, total_penalty: Optional[int] = None):
        print("\n" + "=" * 40)
        print("Результаты поиска пути:")
        print("=" * 40)

        if not optimal_path:
            print("\nПуть не найден.")
            return

        if total_penalty is not None:
            print(f"\nСуммарный штраф: {total_penalty}")

        print("\nПолный путь:")
        for i, state in enumerate(optimal_path):
            to_print = ""
            to_print += f"{i + 1}. {state}"
            if i < len(optimal_path) - 1:
                dx = optimal_path[i + 1].x - state.x
                dy = optimal_path[i + 1].y - state.y
                if dx > 0:
                    to_print += "| Поворот: Вниз"
                elif dx < 0:
                    to_print += "| Поворот: Вверх"
                elif dy > 0:
                    to_print += "| Поворот: Вправо"
                else:
                    to_print += "| Поворот: Влево"
            print(to_print)