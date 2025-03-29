import pytest
from src.CubeProblem import CubeProblem

def test_problem_initialization():
    grid = [[1, 2], [3, 4]]
    face_values = [1, 2, 3, 4, 5, 6]
    problem = CubeProblem(grid, face_values, (0, 0), (1, 1))
    assert problem.grid == grid
    assert problem.start_pos == (0, 0)

def test_invalid_face_values():
    with pytest.raises(ValueError):
        CubeProblem([[1]], [1, 2, 3], (0, 0), (0, 0))