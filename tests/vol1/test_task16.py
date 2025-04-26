from src.vol1.task16 import Task16_vol1

task = Task16_vol1()


class Test:
    def test_1(self):
        large = [50, 20, 100, 10, 30, 25, 22, 33, 35]
        small = [50, 20, 100, 10, 30, 25, 22, 33]
        result = task.execute(large, small)
        expected = ('Possible', 50)
        assert result == expected

    def test_2(self):
        large = [80, 50, 40, 60, 100, 90, 110]
        small = [80, 50, 40, 100, 90, 110]
        result = task.execute(large, small)
        expected = ('Possible', 80)
        assert result == expected

    def test_3(self):
        large = [80, 50, 40, 60, 100, 90, 110]
        small = [80, 50, 60, 100, 90, 110]
        result = task.execute(large, small)
        expected = ('Possible', 50)
        assert result == expected

    def test_4(self):
        large = [80, 50, 40, 60, 100, 90, 110]
        small = [80, 50, 40, 60, 90, 110]
        result = task.execute(large, small)
        expected = ('Possible', 100)
        assert result == expected

    def test_5(self):
        large = [80, 50, 40, 60, 100, 90, 110]
        small = [80, 50, 40, 60, 100, 90]
        result = task.execute(large, small)
        expected = ('Possible', 110)
        assert result == expected

    def test_5(self):
        large = [80, 50, 40, 60, 100, 90, 110]
        small = [80, 50, 40, 60, 70, 100]
        result = task.execute(large, small)
        expected = ('Impossible', None)
        assert result == expected