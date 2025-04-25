from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CubeProblem:
    grid: List[List[int]]
    face_values: List[int]
    start_pos: Tuple[int, int]
    end_pos: Tuple[int, int]