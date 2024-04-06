class Triugolnik:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        d = self.a + self.b + self.c
        return d

    def type(self):
        if self.a == self.b and self.a == self.c:
            return 'равносторонний'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'равнобедренный'
        else:
            return 'разносторонний'

t = Triugolnik(3, 3, 5)
print(f"Периметр треугольника {t.perimeter()}")
print(f"Треугольник {t.type()}")

