import unittest

from mondrian import mondrian


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
        # print result
        # print eval_r
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
        # print result
        # print eval_r
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
        # print result
        # print eval_r
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
        # print result
        # print eval_r
        self.assertTrue(abs(eval_r[0] - 700.0 / 54) < 0.05)

if __name__ == '__main__':
    unittest.main()
