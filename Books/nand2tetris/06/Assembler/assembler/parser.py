import enum

from assembler.code import Code
from assembler.symbol_table import SymbolTable
from assembler.file_handler import FileHandler

class CommandType(enum.Enum):
    A_COMMAND = 'A_COMMAND'
    C_COMMAND = 'C_COMMAND'
    L_COMMAND = 'L_COMMAND'

class Parser:
    def __init__(self, commands):

        self._commands = commands
        self._command_length = len(self._commands)
        self._command_index = 0
        self._symbol_table = SymbolTable()

    @property
    def current_command(self):
        return self._commands[self._command_index]

    @property
    def has_more_commands(self) -> bool:
        return self._command_index < self._command_length

    @property
    def command_type(self):
        if self.current_command[0] == '@':
            return CommandType.A_COMMAND

        if self.current_command[0] == '(':
            return CommandType.L_COMMAND

        return CommandType.C_COMMAND

    def reset(self):
        self._command_index = 0

    def advance(self):
        self._command_index += 1
        if self.has_more_commands:
            self._command = self.current_command

    @staticmethod
    def _get_symbol_or_number_from_command_type_a(command):
        return command.replace('@', '')

    def _parse_command_type_a(self):
        symbol_or_number = self._get_symbol_or_number_from_command_type_a(self.current_command)
        number = None
        print(f'    PARSING A command - {self.current_command} -> {symbol_or_number}')

        try:
            number = int(symbol_or_number)
        except ValueError:
            if self._symbol_table.contains(symbol_or_number):
                number = self._symbol_table.get_address(symbol_or_number)
            else:
                number = self._symbol_table.add_entry(symbol_or_number)
            print(f'        SYMBOL - Get symbol ({symbol_or_number}) from address. Response: {number}\n')

        binary = bin(number)
        raw_binary = binary[2:]
        return '0' * (16 - len(raw_binary)) + raw_binary

    def _parse_command_type_c(self):
        print(f'    PARSING C command - {self.current_command}')
        code = Code(self._command)
        return '111' + code.comp + code.dest + code.jump

    @staticmethod
    def _get_symbol_from_command_type_l(command):
        return command.replace('(', '').replace(')','')


    def parse_to_binary(self):
        if self.command_type == CommandType.A_COMMAND:
            return self._parse_command_type_a()
        if self.command_type == CommandType.C_COMMAND:
            return self._parse_command_type_c()

    def _first_pass(self):
        """This method passes through all commands and gets all the symbols
        To do it, it needs a new pointer to track the "real" commands, meaning 
        the commands which are in the final .hack file.
        
        We only need to watch for A and L commands types since they are the only ones
        that may use symbols
        """
        self._command_index = 0 
        command_real_index = 0
        print('************ FIRST PASS')
        while self.has_more_commands:
            if self.command_type == CommandType.L_COMMAND:
                symbol = self._get_symbol_from_command_type_l(self.current_command)
                print(f'    COMMAND_L - raw_command: {self.current_command}; formatted_command: {symbol}; real_index: {command_real_index}')
                self._symbol_table.add_entry(symbol=symbol, value=command_real_index)
            else:
                print(f'    COMMAND A OR C - {self.current_command}')
                command_real_index += 1
            self.advance()

    def _second_pass(self):
        binaries = []
        self._command_index = 0
        print('************ SECOND PASS')
        while self.has_more_commands:
            binary = self.parse_to_binary()
            if binary:
                binaries.append(binary)
            self.advance()
        return binaries

    def parse(self):
        self._first_pass()
        return self._second_pass()

if __name__ == '__main__':
    commands = FileHandler.load_and_clean_commands('Prog.asm')
    parser = Parser(commands)
    print(parser._commands)
    print(parser._command_length)
    print(parser.parse())