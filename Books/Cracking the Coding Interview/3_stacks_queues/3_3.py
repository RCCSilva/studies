class SetOfStacks:
    def __init__(self, max_itens):
        self.max_itens = max_itens
        self.index = 0
        self.__stack_list = [[]]

    @property
    def __current_stack(self):
        return self.__stack_list[self.index]

    def pop(self):
        while len(self.__current_stack) == 0 and len(self.__stack_list) > 1:
            self.__stack_list.pop()
            self.index -= 1

        return self.__current_stack.pop()

    def pop_at(self, index):
        if index >= len(self.__stack_list):
            raise Exception()

        if len(self.__stack_list[index]) == 0:
            raise Exception()

        return self.__stack_list[index].pop()

    def push(self, value):
        if len(self.__current_stack) == self.max_itens:
            self.index += 1
            self.__stack_list.append([])

        self.__current_stack.append(value)

    def __str__(self):
        return str(self.__stack_list)

if __name__ == '__main__':
    sos = SetOfStacks(3)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    print(sos)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    print(sos)
    sos.pop_at(0)
    sos.pop_at(0)
    sos.pop_at(0)
    print(sos)
    sos.pop()
    print(sos)
    sos.pop()
    print(sos)
    sos.pop()
    print(sos)
    sos.pop()
    print(sos)