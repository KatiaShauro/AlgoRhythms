import unittest
from src.vol3.task26.BlackBox import BlackBox

class TestBlackBox(unittest.TestCase):
    def test_example_from_table(self):
        bb = BlackBox()
        bb.add(3)
        self.assertEqual(bb.get(), 3)
        bb.add(1)
        self.assertEqual(bb.get(), 3)
        bb.add(-4)
        bb.add(2)
        bb.add(8)
        bb.add(-1000)
        self.assertEqual(bb.get(), 1)
        self.assertEqual(bb.get(), 2)

    def test_negative_numbers(self):
        bb = BlackBox()
        bb.add(-5)
        bb.add(-3)
        self.assertEqual(bb.get(), -5)
        self.assertEqual(bb.get(), -3)

    def test_duplicates(self):
        bb = BlackBox()
        bb.add(4)
        bb.add(4)
        bb.add(4)
        self.assertEqual(bb.get(), 4)
        self.assertEqual(bb.get(), 4)
        self.assertEqual(bb.get(), 4)

    def test_mixed_operations(self):
        bb = BlackBox()
        bb.add(10)
        bb.add(20)
        self.assertEqual(bb.get(), 10)
        bb.add(5)
        self.assertEqual(bb.get(), 10)
        self.assertEqual(bb.get(), 20)

if __name__ == '__main__':
    unittest.main()