from typing import Self
from loguru import logger

from symbols import Symbol

class Player:
    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol
        
    def connect_to_game(self, game: "Game"):
        self.connected_game = game
        
    def send_move_to_game(self, i, j):
        self.connected_game.receive_player_move(self, i, j)
    
    def request_undo(self):
        self.connected_game.undo_requested(self)
    
    def recieve_error_message(self, message: str):
        logger.error(f"Player {self.name} ({str(self.symbol)}): {message}")
        
    def recieve_success_message(self, message: str):
        logger.success(f"Player {self.name} ({str(self.symbol)}): {message}")
        
    def __repr__(self) -> str:
        return f'Player("{self.name}", {self.symbol})'
    
    