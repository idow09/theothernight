from abc import ABC, abstractmethod


class UI(ABC):
    def pick_from_list(self, list_, message, count=1):
        self.put_output(message)
        m = ""
        for i in range(len(list_)):
            m += "[{}:{}]".format(i, list_[i])
        m += "\n"
        inp = self.get_input(m)
        if count is 1:
            return list_[int(inp)]
        inp = inp.split(',')
        # return [list_[int(inp[i])] for i in range(count)]
        return list(map(lambda i_: list_[i_], map(int, inp)))

    @abstractmethod
    def get_input(self, message):
        pass

    @abstractmethod
    def put_output(self, message):
        pass


class ConsoleUI(UI):
    def get_input(self, message):
        return input(message)

    def put_output(self, message):
        print(message)
