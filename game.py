from typing import List, Optional
from symbols import X, O
from loguru import logger

from board import Board
from player import Player
from gamelogic import GameLogic
from game_history import GameHistory


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players: List[Player] = []
        self.total_moves: int = 0
        self.current_player: Optional[Player] = None
        self.gamelogic = GameLogic(self)
        self.game_ended: bool = False
        self.game_history = GameHistory(self)
    
    def new_player(self, name: str) -> Player:
        if len(self.players) >= 2:
            logger.error("Can't add new player. Too many players.")
            return
        elif len(self.players) == 0:
            new_player = Player(name, X)
            new_player.connect_to_game(self)
        elif len(self.players) == 1:
            new_player = Player(name, O)
            new_player.connect_to_game(self)
        self.players.append(new_player)
        return new_player
    
    def new_game(self) -> None:
        if len(self.players) != 2:
            logger.error("Not enough players to start game")
            return
        self.board = Board()
        self.game_ended = False
        self.total_moves = 0
        self.current_player = self.players[0]
    
    def undo_requested(self, player):
        previous_player = self.game_history.get_last_player()
        if previous_player is not player:
            player.recieve_error_message("Previous turn not played by you")
            return
        else:
            self.game_history.undo()
            self.current_player = self.game_history.get_last_player()
            self.is_ended = False
    
    def print_board(self) -> None:
        message = str(self.board)
        logger.info("Current game state:")
        logger.info('\n' + message)
    
    def move_to_next_player(self) -> None:
        self.current_player = self.players[self.total_moves % 2]
        
    def receive_player_move(self, player: Player, i: int, j: int):
        try:
            self.gamelogic.check_move_is_valid(player, i, j)
        except Exception as e:
            player.recieve_error_message(e)
        else:
            self.gamelogic.make_move(player, i, j)
            is_game_ended, message = self.gamelogic.check_end()
            if is_game_ended:
                self.game_ended = True
                for player in self.players:
                    player.recieve_success_message(message)
            else:
                self.move_to_next_player()
