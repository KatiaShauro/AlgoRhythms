from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CubeProblem:
    grid: List[List[int]]
    face_values: List[int]
    start_pos: Tuple[int, int]
    end_pos: Tuple[int, int]

    def __post_init__(self):
        if len(self.face_values) != 6:
            raise ValueError("face_values must contain exactly 6 elements")