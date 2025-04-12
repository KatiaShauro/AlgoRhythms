import pytest
from typing import List, Tuple
from your_module import task34_vol2  # Замените на имя вашего файла без .py

@pytest.fixture
def solver():
    return task34_vol2()

def test_empty_list(solver):
    assert solver.dp_solution([]) == (0, 0)

def test_balanced_pairs(solver):
    # (3, 3), (5, 5) → a - b = 0, суммарная разность 0
    arr = [(3, 3), (5, 5)]
    assert solver.dp_solution(arr) == (0, 0)

def test_one_difference(solver):
    # (5, 3), (3, 5) → delta = [2, -2], можно уравновесить
    arr = [(5, 3), (3, 5)]
    assert solver.dp_solution(arr) == (1, 0)

def test_minimal_diff_nonzero(solver):
    # (5, 3), (3, 4) → delta = [2, -1] → можно добиться минимальной разности 1
    arr = [(5, 3), (3, 4)]
    assert solver.dp_solution(arr) == (1, 1)

def test_all_positive_deltas(solver):
    arr = [(5, 1), (6, 2), (4, 2)]  # delta = [4, 4, 2], sum = 10
    # нет способа сделать разность нулевой, но минимально можно
    assert solver.dp_solution(arr) == (1, 2)

def test_all_negative_deltas(solver):
    arr = [(1, 5), (2, 6), (2, 4)]  # delta = [-4, -4, -2], sum = -10
    assert solver.dp_solution(arr) == (1, 2)

def test_complex_case(solver):
    arr = [(5, 3), (4, 4), (2, 3), (3, 1)]  # delta = [2, 0, -1, 2]
    assert solver.dp_solution(arr) == (1, 1)
