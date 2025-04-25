import pytest
from src.vol3.task25.CubePathFinder import CubePathFinder
from src.vol3.task25.CubeState import CubeState

@pytest.fixture
def sample_finder():
    grid = [[1, 2], [3, 4]]
    face_values = [1, 2, 3, 4, 5, 6]
    return CubePathFinder(grid, face_values)

def test_generate_orientations(sample_finder):
    orientations = set(sample_finder.generate_all_orientations())
    assert len(orientations) == 24

def test_get_neighbors(sample_finder):
    state = CubeState(0, 0, 1, 2, 3)
    neighbors = sample_finder.get_neighbors(state)
    assert len(neighbors) == 2
    assert all(isinstance(n[0], CubeState) for n in neighbors)

def test_bfs_uniform_penalty():
    grid = [[1, 1], [1, 1]]
    face_values = [1, 1, 1, 1, 1, 1]
    finder = CubePathFinder(grid, face_values)
    penalty, path = finder.find_optimal_path((0, 0), (1, 1))

    assert penalty == 0
    assert len(path) == 3

def test_bfs_variable_penalty():
    grid = [[2, 3], [4, 5]]
    face_values = [1, 2, 3, 4, 5, 6]
    finder = CubePathFinder(grid, face_values)
    penalty, path = finder.find_optimal_path((0, 0), (1, 1))

    assert penalty == sum(
        abs(grid[x][y] - face_values[state.top - 1]) for (x, y), state in zip([(0, 0), (0, 1), (1, 1)], path))