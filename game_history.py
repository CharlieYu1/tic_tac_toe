from loguru import logger

class GameHistory:
    def __init__(self, game: "Game") -> None:
        self._game = game
        self.history = []
    
    def clear_history(self) -> None:
        self.history = []
    
    def add_to_history(self, player: "Player", i: int, j: int) -> None:
        self.history.append([player, i, j])
        
    def undo(self) -> None:
        player, i, j = self.history.pop()
        self._game.board.get_spot(i, j).clear()
        self._game.total_moves -= 1     
    
    def get_last_player(self) -> "Player":
        if len(self.history) == 0:
            return None
        else:
            return self.history[-1][0]
        
    def print_history(self) -> None:
        logger.info(f"Game History: {self.history}")