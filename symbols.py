from typing import Literal, Self

SymbolLiteral = Literal['X', 'O']

class Symbol:
    def __init__(self, symbol: SymbolLiteral) -> None:
        self.symbol = symbol
    
    def __str__(self) -> str:
        return self.symbol
    
    def __repr__(self) -> str:
        return f"Symbol({self.symbol})"
    
    def __eq__(self, other: Self) -> bool:
        return self.symbol == other.symbol
    
X = Symbol('X')
O = Symbol('O')