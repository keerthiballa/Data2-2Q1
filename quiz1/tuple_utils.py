from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]


def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:
    """
    This function takes in a TicTacToeBoard and applies the finishing move based on the provided parameters pos_y,
    pos_x, and symbol.
    :param board: A tuple containing 3 TicTacToeRows. Each TicTacToeRow in turn is a list containing 3 strings
    :param pos_y: The position of the TicTacToeRow that needs to be modified
    :param pos_x: The position of the column within a TicTacToeRow that needs to be modified
    :param symbol: The symbol that should be placed in the column (X, or O)
    :return: None
    """
    board[pos_y][pos_x] = symbol
    return board

def count_things(collection: Tuple, thing: Union[int, str]) -> int:
    """
    This function counts the number of occurrences of the thing value within the collection parameter.
    :param collection: A tuple containing 0 or more things
    :param thing: An item in the collection parameter
    :return: An integer.
    """
    return collection.count(thing)


def produce_tuple(alist: List) -> Tuple:
    """
    Produce a specific tuple.
    """
    return tuple(alist)
    #print(result)


#produce_tuple(['a','b','c'])

#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 % python3 -m unittest quiz1.test_tuple_utils
#..F..
#======================================================================
#FAIL: test_produce_tuple (quiz1.test_tuple_utils.TupleUtilsTest)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "/Users/ballakeerthi/dev/Data2-2Q1/quiz1/test_tuple_utils.py", line 50, in test_produce_tuple
#    self.assertEqual(expected, actual)
#AssertionError: Tuples differ: ('Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth') != ()
#
#First tuple contains 7 additional elements.
#First extra element 0:
#'Pride'

#- ('Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth')
#+ ()

#----------------------------------------------------------------------
#Ran 5 tests in 0.001s

#FAILED (failures=1)
#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 %
