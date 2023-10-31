from typing import Tuple

from spot import Spot
from symbols import Symbol

BoardType = Tuple[
                Tuple[Spot, Spot, Spot],
                Tuple[Spot, Spot, Spot],
                Tuple[Spot, Spot, Spot],
            ]

class Board:
    def __init__(self) -> None:
        self._board: BoardType = [
            [Spot() for i in range(3)] for j in range(3)
        ]
    
    def __str__(self) -> str:
        output = ''
        output += f'{str(self._board[0][0])}|{str(self._board[0][1])}|{str(self._board[0][2])}\n'
        output += f'-+-+-\n'
        output += f'{str(self._board[1][0])}|{str(self._board[1][1])}|{str(self._board[1][2])}\n'
        output += f'-+-+-\n'
        output += f'{str(self._board[2][0])}|{str(self._board[2][1])}|{str(self._board[2][2])}\n'
        return output
    
    def get_spot(self, i: int, j: int):
        return self._board[i][j]
    
    def check_complete_line(self, symbol):
        lines = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)],
        ]
        for line in lines:
            if all(self.get_spot(i, j).contains(symbol) for i, j in line):
                return True
        return False
        
        