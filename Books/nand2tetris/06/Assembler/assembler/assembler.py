from assembler.parser import Parser
from assembler.file_handler import FileHandler

class Assembler:
    def __init__(self, file_path):
        self._file_path = file_path
        self._raw_commands = FileHandler.load_and_clean_commands(file_path)
        self._parser = Parser(self._raw_commands)

    def assemble(self):
        binaries = self._parser.parse()
        with open(self._file_path.replace('.asm', '.hack'), 'w') as file:
            file.write('\n'.join(binaries))

if __name__ == '__main__':
    assembler = Assembler('Prog.asm')
    assembler.assemble()