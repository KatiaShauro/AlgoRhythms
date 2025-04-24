from src.vol2.Task34 import Task34_vol2


task = Task34_vol2()


class TestDp:
    def test_1(self):
        dominoes = [(6, 1), (1, 5), (1, 3), (1, 2)]
        expected = (1, 0)
        result = task.dp_solution(dominoes)
        assert result == expected

    def test_2(self):
        dominoes = [(1, 1), (2, 2)]
        expected = (0, 0)
        result = task.dp_solution(dominoes)
        assert result == expected

    def test_3(self):
        dominoes = [(3, 5), (2, 4), (1, 6)]
        expected = (1, 1)
        result = task.dp_solution(dominoes)
        assert result == expected


class TestGreedy:
    def test_1(self):
        dominoes = [(6, 1), (1, 5), (1, 3), (1, 2)]
        expected = (1, 0)
        result = task.greedy_solution(dominoes)
        assert result == expected

    def test_2(self):
        dominoes = [(1, 1), (2, 2)]
        expected = (0, 0)
        result = task.greedy_solution(dominoes)
        assert result == expected

    def test_3(self):
        dominoes = [(3, 5), (2, 4), (1, 6)]
        expected = (1, 1)
        result = task.greedy_solution(dominoes)
        assert result == expected


class TestBruteForce:
    def test_1(self):
        dominoes = [(6, 1), (1, 5), (1, 3), (1, 2)]
        expected = (1, 0)
        result = task.brute_force_solution(dominoes)
        assert result == expected

    def test_2(self):
        dominoes = [(1, 1), (2, 2)]
        expected = (0, 0)
        result = task.brute_force_solution(dominoes)
        assert result == expected

    def test_3(self):
        dominoes = [(3, 5), (2, 4), (1, 6)]
        expected = (1, 1)
        result = task.brute_force_solution(dominoes)
        assert result == expected
