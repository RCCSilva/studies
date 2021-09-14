from assembler.assembler import Assembler

if __name__ == '__main__':
    assembler = Assembler('Prog.asm')
    print(assembler._raw_commands)
    print(assembler._parser._commands)
    assembler.assemble()
