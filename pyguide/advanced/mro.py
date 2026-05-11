"""
Demonstration of Python Method Resolution Order (MRO).

MRO determines the order in which base classes are searched when
looking for a method, especially important in multiple inheritance.
"""


class A:
    def greet(self):
        return "Hello from A"


class B(A):
    def greet(self):
        return "Hello from B"


class C(A):
    def greet(self):
        return "Hello from C"


class D(B, C):
    """Diamond inheritance: D inherits from B and C, both inherit from A."""
    pass


class E(C, B):
    """Same parents as D but reversed order."""
    pass


class F(D):
    def greet(self):
        return "Hello from F, parent says: " + super().greet()


def main() -> None:
    # MRO for simple inheritance
    assert A.__mro__ == (A, object)
    assert B.__mro__ == (B, A, object)

    # Diamond inheritance MRO (C3 linearization)
    assert D.__mro__ == (D, B, C, A, object)

    # Reversed order gives different MRO
    assert E.__mro__ == (E, C, B, A, object)

    # Method resolution follows MRO
    d = D()
    assert d.greet() == "Hello from B"  # B is first in MRO after D

    e = E()
    assert e.greet() == "Hello from C"  # C is first in MRO after E

    # super() follows MRO
    f = F()
    result = f.greet()
    assert "Hello from F" in result
    assert "Hello from B" in result  # B is next in F's MRO

    # Explicit super with class argument
    class G(B, C):
        def greet(self):
            # Explicitly start MRO lookup from C
            return "G says: " + super(B, self).greet()

    g = G()
    assert "Hello from C" in g.greet()

    # MRO ensures each class appears only once
    for cls in D.__mro__:
        count = D.__mro__.count(cls)
        assert count == 1, f"{cls} appears {count} times"

    # mro() method returns same as __mro__
    assert D.mro() == list(D.__mro__)


if __name__ == "__main__":
    main()
