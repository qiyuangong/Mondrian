# coding:utf-8
from datetime import datetime
import unittest

from mondrian import mondrian
from utils.read_file import read_csv

class functionTest(unittest.TestCase):
    def test1_mondrian_strict(self):
        data = [[6, 1, 'haha'],
                [6, 1, 'test'],
                [8, 2, 'haha'],
                [8, 2, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, False)
        self.assertTrue(abs(eval_r[0] - 100.0 / 12) < 0.05)

    def test1_mondrian_relax(self):
        data = [[6, 1, 'haha'],
                [6, 1, 'test'],
                [8, 2, 'haha'],
                [8, 2, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, True)
        self.assertTrue(abs(eval_r[0] - 100.0 / 12) < 0.05)

    def test2_mondrian_strict(self):
        data = [[6, 1, 'haha'],
                [8, 1, 'haha'],
                [8, 1, 'test'],
                [8, 1, 'haha'],
                [8, 1, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, False)
        self.assertTrue(abs(eval_r[0] - 2300.0 / 108) < 0.05)

    def test2_mondrian_relax(self):
        data = [[6, 1, 'haha'],
                [8, 1, 'haha'],
                [8, 1, 'test'],
                [8, 1, 'haha'],
                [8, 1, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, True)
        self.assertTrue(abs(eval_r[0] - 700.0 / 54) < 0.05)

    def test_mondrian_datetime(self):
        d1 = datetime.strptime("2007-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime("2008-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
        d3 = datetime.strptime("2009-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
        d4 = datetime.strptime("2007-03-05 21:08:12", "%Y-%m-%d %H:%M:%S")
        data = [[6, d1, 'haha'],
                [8, d1, 'haha'],
                [8, d1, 'test'],
                [8, d1, 'haha'],
                [8, d1, 'test'],
                [4, d1, 'hha'],
                [4, d2, 'hha'],
                [4, d3, 'hha'],
                [4, d4, 'hha']]
        result, eval_r = mondrian(data, 2, False)
        print(eval_r)

    def test_read_csv_and_anonymise(self):
        from utils.read_adult_data import read_data as read_adult
        DATA, INTUITIVE_ORDER = read_adult() 
        result, eval_result = mondrian(DATA, 40, False)
        print(result)

if __name__ == '__main__':
    unittest.main()
