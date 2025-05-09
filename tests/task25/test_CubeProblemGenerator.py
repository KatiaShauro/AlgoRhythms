import pytest
from src.vol3.task25.CubeProblemGenerator import CubeProblemGenerator

def test_generate_field():
    field = CubeProblemGenerator.generate_field(2, 2)
    assert len(field) == 2
    assert all(len(row) == 2 for row in field)

def test_generate_positions():
    start, end = CubeProblemGenerator.generate_positions(3, 3)
    assert start != end