import pytest
from src.CubePathFinder import CubePathFinder
from src.CubeState import CubeState

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