class Code:
    def __init__(self, code):
        self._code = code
        self._dest = ''
        self._comp = ''
        self._jump = ''
        self.parse()

    def parse(self):
        comp = ''
        dest = ''
        jump = ''
        temp = ''
        for x in self._code:
            if x == '=':
                self._dest = temp
                temp = ''
            elif x == ';':
                self._comp = temp
                temp = ''
            else:
                temp += x
        if self._comp:
            self._jump = temp
        else:
            self._comp = temp

    @property
    def dest(self):
        dest_table = {
            '':'000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
        }
        return dest_table[self._dest]

    @property
    def comp(self):
        comp_place_holder = self._comp.replace('A','@').replace('M', '@') # use @ as a placeholder for M and A
        comp_table = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            '@': '110000',
            '!D': '001101',
            '!@': '110001',
            '-D': '001111',
            '-@': '110011',
            'D+1': '011111',
            '@+1': '110111',
            'D-1': '001110',
            '@-1': '110010',
            'D+@': '000010',
            'D-@': '010011',
            '@-D': '000111',
            'D&@': '000000',
            'D|@': '010101'
        }

        prefix = '0' if self._comp.find('M') == -1 else '1'

        return prefix + comp_table[comp_place_holder]

    @property
    def jump(self):
        jump_table = {
            '': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }
        return jump_table[self._jump]

if __name__ == '__main__':
    code = Code('D;JGT')
    print('dest: ', code.dest)
    print('comp: ', code.comp)
    print('jump: ', code.jump)