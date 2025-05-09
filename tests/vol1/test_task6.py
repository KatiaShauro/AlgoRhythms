from src.vol1.task6 import Task6_vol1

task = Task6_vol1()

class Test:
    def test_1(self):
        tree = [50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40, 100, 120]
        result = task.first_part_of_solution(tree)
        expected = "40 37 35 33 30 20 50 100 120 | 50"
        assert result == expected


    def test_2(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 100, 120, 130, 140]
        result = task.first_part_of_solution(tree)
        expected = "7 8 9 10 20 50 100 120 130 140 | 50"
        assert result == expected


    def test_3(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 100]
        result = task.first_part_of_solution(tree)
        expected = "7 8 9 10 20 30 25 22 | 20"
        assert result == expected


    def test_4(self):
        tree = [50, 20, 10, 9, 30, 29, 28, 27, 33, 35, 34, 37, 40]
        result = task.first_part_of_solution(tree)
        expected = "27 28 29 30 33 35 37 40 | 30"
        assert result == expected


    def test_5(self):
        tree = [50, 20, 10, 30, 25, 22, 33, 100, 120, 130]
        result = task.first_part_of_solution(tree)
        expected = "22 25 30 20 50 100 120 130 | 50"
        assert result == expected


    def test_6(self):
        tree = [50, 20, 10, 9, 8, 7, 30, 25, 22, 33, 35, 40, 100]
        result = task.first_part_of_solution(tree)
        expected = "7 8 9 10 20 30 33 35 40 | 20"
        assert result == expected


    def test_7(self):
        tree = [50, 20, 10, 30, 100, 80, 60, 90, 91, 92, 110, 120, 130, 105]
        result = task.first_part_of_solution(tree)
        expected = "92 91 90 80 100 110 120 130 | 100"
        assert result == expected


    def test_8(self):
        tree = [50, 20, 10, 30, 60, 70, 65, 80, 64, 63, 62, 61, 90, 75, 100, 95, 97]
        result = task.first_part_of_solution(tree)
        expected = "61 62 63 64 65 70 80 90 100 95 97 | 70"
        assert result == expected


    def test_9(self):
        tree = [50, 20, 10, 30, 60, 70, 65, 80, 64, 63, 62, 61, 90, 75, 100, 95, 97, 5]
        result = task.first_part_of_solution(tree)
        expected = "61 62 63 64 65 70 80 90 100 95 97 | 70"
        assert result == expected


    def test_10(self):
        tree = [50, 20, 10, 9, 30, 29, 33, 35, 34, 37, 28, 27, 25, 40]
        result = task.first_part_of_solution(tree)
        expected = "25 27 28 29 30 33 35 37 40 | 30"
        assert result == expected


    def test_11(self):
        tree = [50, 20, 10, 30]
        result = task.first_part_of_solution(tree)
        expected = "30 20 50 | 50"
        assert result == expected


    def test_12(self):
        tree = [50, 20, 10, 25, 8, 100, 90, 80]
        result = task.first_part_of_solution(tree)
        expected = "8 10 20 50 100 90 80 | 50"
        assert result == expected


    def test_13(self):
        tree = [50, 20, 10, 25, 8, 100, 90]
        result = task.first_part_of_solution(tree)
        expected = "8 10 20 50 100 90 | 50"
        assert result == expected


    def test_14(self):
        tree = []
        result = task.first_part_of_solution(tree)
        expected = ""
        assert result == expected


    def test_15(self):
        tree = [50]
        result = task.first_part_of_solution(tree)
        expected = "50 | 50"
        assert result == expected


    def test_16(self):
        tree = [50, 40, 30, 20, 10]
        result = task.first_part_of_solution(tree)
        expected = "10 20 30 40 50 | 50"
        assert result == expected


    def test_17(self):
        tree = [10, 20, 30, 40, 50]
        result = task.first_part_of_solution(tree)
        expected = "10 20 30 40 50 | 10"
        assert result == expected


    def test_18(self):
        tree = [50, 30, 70, 20, 40, 60, 80]
        result = task.first_part_of_solution(tree)
        expected = "40 30 50 70 80 | 50"
        assert result == expected


    def test_19(self):
        tree = [100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 130, 160, 200]
        result = task.first_part_of_solution(tree)
        expected = "90 75 50 100 150 175 200 | 100"
        assert result == expected

