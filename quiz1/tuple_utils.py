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
    pass  # remove pass statement and implement me


def count_things(collection: Tuple, thing: Union[int, str]) -> int:
    """
    This function counts the number of occurrences of the thing value within the collection parameter.
    :param collection: A tuple containing 0 or more things
    :param thing: An item in the collection parameter
    :return: An integer.
    """
    pass  # remove pass statement and implement me


def produce_tuple(alist: List) -> Tuple:
    """
    Produce a specific tuple.
    """
    pass # remove pass statement and implement me
