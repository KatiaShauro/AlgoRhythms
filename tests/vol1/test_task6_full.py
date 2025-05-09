from src.vol1.task6 import Task6_vol1

task = Task6_vol1()

class Test:
    def test_1(self):
        tree = [50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40, 100, 120]
        result = task.execute(tree)
        expected = "100 20 10 9 33 29 28 27 35 34 37 40 120 "
        assert result == expected


    def test_2(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 100, 120, 130, 140]
        result = task.execute(tree)
        expected = "100 20 10 9 8 7 30 25 22 33 120 130 140 "
        assert result == expected


    def test_3(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 100]
        result = task.execute(tree)
        expected = "50 22 10 9 8 7 30 25 33 100 "
        assert result == expected


    def test_4(self):
        tree = [50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40]
        result = task.execute(tree)
        expected = "50 20 10 9 33 29 28 27 35 34 37 40 "
        assert result == expected


    def test_5(self):
        tree = [50, 20, 10, 30, 25, 22, 33, 100, 120, 130]
        result = task.execute(tree)
        expected = "100 20 10 30 25 22 33 120 130 "
        assert result == expected


    def test_6(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 35, 40, 100]
        result = task.execute(tree)
        expected = "50 22 10 9 8 7 30 25 33 35 40 100 "
        assert result == expected


    def test_7(self):
        tree = [50, 20, 10, 30, 100, 80, 60, 90, 91, 92, 110, 120, 130, 105]
        result = task.execute(tree)
        expected = "50 20 10 30 105 80 60 90 91 92 110 120 130 "
        assert result == expected


    def test_8(self):
        tree = [50, 20, 10, 30, 60, 70, 65, 80, 64, 63, 62, 61, 90, 75, 100, 95, 97]
        result = task.execute(tree)
        expected = "50 20 10 30 60 75 65 64 63 62 61 80 90 100 95 97 "
        assert result == expected


    def test_9(self):
        tree = [50, 20, 10, 30, 60, 70, 65, 80, 64, 63, 62, 61, 90, 75, 100, 95, 97, 5]
        result = task.execute(tree)
        expected = "50 20 10 5 30 60 75 65 64 63 62 61 80 90 100 95 97 "
        assert result == expected


    def test_10(self):
        tree = [50, 20, 10, 9, 30, 29, 33, 35, 34, 37, 28, 27, 25, 40, 100]
        result = task.execute(tree)
        expected = "50 20 10 9 33 29 28 27 25 35 34 37 40 100 "
        assert result == expected


    def test_11(self):
        tree = [50, 20, 10, 30]
        result = task.execute(tree)
        expected = "30 10 "
        assert result == expected


    def test_12(self):
        tree = [50, 20, 10, 25, 8, 100, 90, 80]
        result = task.execute(tree)
        expected = "80 20 10 8 25 100 90 "
        assert result == expected


    def test_13(self):
        tree = [50, 20, 10, 25, 8, 100, 90]
        result = task.execute(tree)
        expected = "90 20 10 8 25 100 "
        assert result == expected


    def test_14(self):
        tree = []
        result = task.execute(tree)
        expected = "Empty tree!"
        assert result == expected


    def test_15(self):
        tree = [50]
        result = task.execute(tree)
        expected = ""
        assert result == expected


    def test_16(self):
        tree = [50, 40, 30, 20, 10]
        result = task.execute(tree)
        expected = "40 20 10 "
        assert result == expected


    def test_17(self):
        tree = [10, 20, 30, 40, 50]
        result = task.execute(tree)
        expected = "20 40 50 "
        assert result == expected


    def test_18(self):
        tree = [50, 30, 70, 20, 40, 60, 80]
        result = task.execute(tree)
        expected = "60 30 20 40 70 80 "
        assert result == expected


    def test_19(self):
        tree = [100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 130, 160, 200]
        result = task.execute(tree)
        expected = "110 50 25 10 30 75 60 90 150 125 130 175 160 200 "
        assert result == expected

