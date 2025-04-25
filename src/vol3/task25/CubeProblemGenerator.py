import random
from typing import List, Tuple
from src.vol3.task25.CubeProblem import CubeProblem


class CubeProblemGenerator:
    @staticmethod
    def generate_field(rows: int, cols: int, min_val: int = 1, max_val: int = 9) -> List[List[int]]:
        return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    @staticmethod
    def generate_face_values(min_val: int = 1, max_val: int = 6) -> List[int]:
        values = list(range(min_val, max_val + 1))
        random.shuffle(values)
        return values[:6]

    @staticmethod
    def generate_positions(rows: int, cols: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        positions = [(x, y) for x in range(rows) for y in range(cols)]
        return random.sample(positions, 2)

    @classmethod
    def generate_problem(cls, min_size=3, max_size=5, min_val=1, max_val=9) -> CubeProblem:
        rows = cols = random.randint(min_size, max_size)
        grid = cls.generate_field(rows, cols, min_val, max_val)
        face_values = cls.generate_face_values(min_val, min(max_val, 6))
        start_pos, end_pos = cls.generate_positions(rows, cols)
        return CubeProblem(grid, face_values, start_pos, end_pos)