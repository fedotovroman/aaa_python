from abc import ABC, abstractmethod
import random

class AnimeMon(ABC):
    @abstractmethod
    def inc_exp(self):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    def to_str(self):
        return f'{self.name}/{self.poketype}'

    def inc_exp(self, value):
        self._exp += value

    @property
    def exp(self):
        return self._exp


class Digimon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    def to_str(self):
        return f'{self.name}/{self.poketype}'

    def inc_exp(self, value):
        self._exp += 8 * value

    @property
    def exp(self):
        return self._exp

def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)

def main():
    pikachu = Pokemon(name = 'Pikachu', poketype = 'small')
    train(pikachu)
    print(pikachu.exp)

    digi = Digimon(name = 'Dino', poketype = 'smaller')
    train(digi)
    print(digi.exp)

if __name__ == '__main__':
    main()

