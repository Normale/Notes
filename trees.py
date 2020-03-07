class Operator:
    '''Takes exactly two arguments, left and right in tree.'''
    def __init__(self, l, r):
        self.l = l
        self.r = r
class Times(Operator):
    def __call__(self):
        return self.l() * self.r()
    def __str__(self):
        return f"({self.l} * {self.r})"
    def __repr__(self):
        return f"Times({repr(self.l)},{repr(self.r)})"
class Plus(Operator):
    def __call__(self):
        return self.l() + self.r()
    def __str__(self):
        return f"({self.l} + {self.r})"
    def __repr__(self):
        return f"Plus({repr(self.l)},{repr(self.r)})"
class Const:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"Const({self.value})"
class Var:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Var('{self.name}')"

e1 = Times(Const(3), Plus(Var('y'), Var("x")))
e2 = Times(Const(3), Times(Const(5), Times(Const(3), Var("y"))))
print(repr(e2))
print(e1)