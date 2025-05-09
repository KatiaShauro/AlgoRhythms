import pytest
from src.vol3.task25.CubeProblem import CubeProblem
from src.vol3.task25.CubePathFinder import CubePathFinder

@pytest.fixture
def sample_problem():
    grid = [[1, 2], [3, 4]]
    face_values = [1, 2, 3, 4, 5, 6]
    return CubeProblem(grid, face_values, (0, 0), (1, 1))

@pytest.fixture
def sample_finder(sample_problem):
    return CubePathFinder(sample_problem.grid, sample_problem.face_values)