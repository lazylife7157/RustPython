class Foo:
    def __init__(self, x):
        assert x == 5
        self.x = x

    def square(self):
        return self.x * self.x

    y = 7

foo = Foo(5)

assert foo.y == Foo.y
assert foo.x == 5
assert foo.square() == 25


class Bar:
    @classmethod
    def fubar(cls, x):
        assert cls is Bar
        assert x == 2

    @staticmethod
    def kungfu(x):
        assert x == 3


bar = Bar()
bar.fubar(2)

# TODO: make below work:
# Bar.fubar(2)

bar.kungfu(3)
# TODO: make below work:
# Bar.kungfu(3)

