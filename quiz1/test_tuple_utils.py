import unittest
import unittest.mock
from io import StringIO
from quiz1.tuple_utils import count_things, produce_tuple, tic_tac_toe_finish


class TupleUtilsTest(unittest.TestCase):

    def test_tic_tac_toe_finish(self):
        board_in = (
            ['O', 'X', ''],
            ['X', 'X', ''],
            ['', '', '']
        )
        board_out = (
            ['O', 'X', ''],
            ['X', 'X', 'X'],
            ['', '', '']
        )
        tic_tac_toe_finish(board_in, 1, 2, 'X')
        self.assertEqual(board_in, board_out)

    def test2_tic_tac_toe_finish(self):
        board_in = (
            ['', '', ''],
            ['X', 'O', ''],
            ['X', '', 'O']
        )
        board_out = (
            ['O', '', ''],
            ['X', 'O', ''],
            ['X', '', 'O']
        )
        tic_tac_toe_finish(board_in, 0, 0, 'O')
        self.assertEqual(board_in, board_out)

    def test_count_instances(self):
        test_cases = [
            ((1, 1, 1, 0), 1, 3),
            (('A', 'B', 'B', 'C'), 'B', 2)
        ]
        for tuple_to_evaluate, item_to_count, expected in test_cases:
            with self.subTest(f"{tuple_to_evaluate}, {item_to_count} -> {expected}"):
                self.assertEqual(expected, count_things(tuple_to_evaluate, item_to_count))

    def test_produce_tuple(self):
        expected = ('Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth')
        
        actual = produce_tuple([])
        self.assertEqual(expected, actual)

    def test_produce_tuple2(self):
        expected = ('Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth')
        sins = ['Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth']
        actual = produce_tuple(sins)
        self.assertEqual(expected, actual)
      

