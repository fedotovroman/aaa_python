class LinkedTransform:
    def __init__(self, method, previous_t = None):
        self.method = method
        self.previous_transformation = previous_t

    def create_chain(self):
        transformation_chain = []
        current_transformation = self
        while current_transformation is not None:
            transformation_chain.insert(0, current_transformation.method)
            current_transformation = current_transformation.previous_transformation
        return transformation_chain

    @staticmethod
    def method_from_chain(chain):
        def inner(arg):
            for method in chain:
                arg = method(arg)
            return arg
        return inner

class Seq:
    def __init__(self, seq, tr = None):
        self.seq = seq
        self.transformation = tr

    def map(self, map_method):
        current_transform = LinkedTransform(map_method, self.transformation)
        return Seq(self.seq, current_transform)

    def filter(self, filter_method):

        return Seq(self.seq, current_filter)

    def take(self, n):
        if self.transformation is not None:
            transformation_chain = self.transformation.create_chain()
        else:
            transformation_chain = []

        for take_i, seq_el in zip(range(n), self.seq):
            for method in transformation_chain:

            yield composed_method(seq_el)

def main():
    x = range(100000000)
    seq = Seq(x).map(lambda x: x).take(15)
    for el in seq:
        print(el)


if __name__ == '__main__':
    main()
