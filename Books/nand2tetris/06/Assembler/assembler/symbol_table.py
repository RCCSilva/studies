def load_default_table():
    table = {
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
        'SCREEN': 16384,
        'KBD':  24576
    }
    for x in range(16):
        table[f'R{x}'] = x

    return table

class SymbolTable:
    def __init__(self):
        self._table = load_default_table()
        self.current_address = 16

    def add_entry(self, symbol: str, value: int = None) -> None:
        if value:
            self._table[symbol] = value
            return

        self._table[symbol] = self.current_address
        self.current_address += 1
        return self.current_address - 1

    def contains(self, symbol: str) -> bool:
        return symbol in self._table

    def get_address(self, symbol) -> int:
        return self._table[symbol]


if __name__ == '__main__':
    symbol_table = SymbolTable()
    print(symbol_table._table)