from typing import Optional

from symbols import Symbol

class Spot:
    def __init__(self) -> None:
        self.symbol: Optional[Symbol] = None
        
    def set_symbol(self, symbol: Symbol) -> None:
        self.symbol = symbol
    
    def __str__(self) -> str:
        if self.symbol:
            return str(self.symbol)
        else:
            return ' '
    
    @property
    def is_empty(self) -> bool:
        return self.symbol is None
    
    @property
    def is_occupied(self) -> bool:
        return not self.is_empty
    
    def clear(self) -> None:
        self.symbol = None
        
    def contains(self, symbol: Optional[Symbol]) -> bool:
        if self.is_occupied:
            return self.symbol == symbol
        else:
            return False