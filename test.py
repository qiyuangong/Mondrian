import unittest

from mondrian import mondrian


class functionTest(unittest.TestCase):
    def test_mondrian_strict(self):
        data = [[6, 1, 'haha'],
                [6, 1, 'test'],
                [8, 2, 'haha'],
                [8, 2, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, False)
        self.assertTrue(eval_r[0] - 100 * 5.0 / 24 < 0.05)

    def test_mondrian_relax(self):
        data = [[6, 1, 'haha'],
                [6, 1, 'test'],
                [8, 2, 'haha'],
                [8, 2, 'test'],
                [4, 1, 'hha'],
                [4, 2, 'hha'],
                [4, 3, 'hha'],
                [4, 4, 'hha']]
        result, eval_r = mondrian(data, 2, True)
        self.assertTrue(eval_r[0] - 100 * 5.0 / 24 < 0.05)


if __name__ == '__main__':
    unittest.main()
