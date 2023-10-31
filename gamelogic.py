from typing import Tuple

class GameLogic:
    def __init__(self, game: "Game"):
        self._game = game

    def check_move_is_valid(self, player: "Player", i: int, j: int):
        current_player = self._game.current_player
        if self._game.game_ended:
            raise Exception("Game already ended")
        if player != current_player:
            raise Exception("Not current player")
        if i < 0 or i > 2 or j < 0 or j > 2:
            raise Exception("Chosen coordinates out of range")
        if self._game.board.get_spot(i, j).is_occupied:
            raise Exception("Chosen spot is already occupied")
        
    def make_move(self, player: "Player", i: int, j: int):
        self._game.board.get_spot(i, j).set_symbol(player.symbol)
        self._game.game_history.add_to_history(player, i, j)
        self._game.total_moves += 1
        
    def check_end(self) -> Tuple[bool, str]:
        current_player = self._game.current_player
        current_player_symbol = current_player.symbol
        if self._game.board.check_complete_line(current_player_symbol):
            message = f'{current_player.name} ({current_player.symbol}) wins!'
            return [True, message]
        elif self._game.total_moves == 9:
            return [True, 'Game ends in a draw']
        else:
            return [False, '']
        