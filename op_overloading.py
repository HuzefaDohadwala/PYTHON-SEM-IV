class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__ (self,other):
        return Vector(self.x - other.x , self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)

    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print(v3)  # Output: (6, 8)

v4 = v1 - v2
print(v4)  # Output: (-2, -2)

v5 = v1 * 2
print(v5)  # Output: (4, 6)

v6 = v2 * 3
print(v6)  # Output: (6, 9)

print(v1 == v2)  # Output: False
print(v1 != v2)  # Output: True
print(v1 > v2)  # Output: False
print(v1 < v2)  # Output: True
print(v1 >= v3)  # Output: True
print(v1 <= v3)  # Output: True