from abc import ABC, abstractmethod

class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass

    @staticmethod
    def print_a(color: ComputerColor):
        bg_color = 0.2 * color

        a_matrix = [
           #copy realisation
        ]

        for row in a_matrix:
            print(''.join(str(ptr) for ptr in row))

class Color(ComputerColor):

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __repr__(self):


    def convert_color(selc, c, L):
        cl = -256*(1 - c)
        F = (259*(cl+255))/(255*(259 - cl))
        return F * (L - 128) + 128

    def __init__(self):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def __str__(self):
        return f'{Color.START}; {self.r}; {self.g}; {self.b}{Color.MOD}X{Color.MOD}{Color.END}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):


    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

class HSLColor(ComputerColor):
    def __repr__():
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
