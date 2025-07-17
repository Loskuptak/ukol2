import unittest
from soucet import soucet

class TestSoucet(unittest.TestCase):
    def testset_validnich_inputu(self):
        self.assertEqual(soucet(7, 6), 13)
        self.assertEqual(soucet(-22.5, 22.5), 0)
        self.assertEqual(soucet(0, 0), 0)
        self.assertEqual(soucet(1.256, 2.356), 3.612)
        self.assertEqual(soucet(1_000_000, 2_000_000), 3_000_000)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            soucet("f", 5)
        with self.assertRaises(ValueError):
            soucet(22, None)
        with self.assertRaises(ValueError):
            soucet([], 6)
        with self.assertRaises(ValueError):
            soucet({}, 5)
        with self.assertRaises(ValueError):
            soucet([21, 100], [23, 44])
        with self.assertRaises(ValueError):
            soucet(True, 66)

    def test_result_types(self):
        self.assertIsInstance(soucet(22, 23), int)
        self.assertIsInstance(soucet(2.25, 321.5), float)
        self.assertTrue(isinstance(soucet(8, 36.5), (int, float)))
        
if __name__ == '__main__':
    unittest.main()
