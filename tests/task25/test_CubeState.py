import pytest
from src.vol3.task25.CubeState import CubeState

def test_cube_state_creation():
    state = CubeState(x=1, y=2, top=3, front=4, right=5)
    assert state.x == 1
    assert state.y == 2
    assert state.top == 3

def test_cube_state_equality():
    state1 = CubeState(1, 2, 3, 4, 5)
    state2 = CubeState(1, 2, 3, 4, 5)
    assert state1 == state2

def test_cube_state_lt():
    state1 = CubeState(1, 1, 1, 1, 1)
    state2 = CubeState(2, 2, 2, 2, 2)
    assert state1 < state2