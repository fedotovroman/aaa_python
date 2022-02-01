from __future__ import annotations
import typing as t
from itertools import islice


class Seq:
    """
    Description: This class is a funny copy of the Sequence class from the pyfunctional module

    """
    def __init__(self, seq: t.Sequence):
        self.seq = seq

    def transform(self, transformation: t.Callable, method: t.Callable, seq: t.Sequence) -> Seq:
        transformed = transformation(method, seq)
        return Seq(transformed)

    def map(self, method: t.Callable) -> Seq:
        return self.transform(map, method, self.seq)

    def filter(self, method: t.Callable) -> Seq:
        return self.transform(filter, method, self.seq)

    def take(self, n: int) -> list:
        slice = islice(self.seq, 0, n)
        return list(slice)

def main():
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).take(3)
    assert res == [2, 4]

if __name__ == '__main__':
    main()

