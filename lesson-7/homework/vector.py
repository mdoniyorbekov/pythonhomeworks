class Vector:
    def __init__(self, *components):
        self.components = tuple(components)
    def __str__(self):
        return f"Vector{self.components}"
    def __add__ (self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Values must have the same dimension as its addition")
        return Vector(*(a+b for a, b in zip(self.components, other.components)))
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for substraction")
        return Vector(*(a-b for a, b in zip(self.components, other.components)))
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors should have the same dimensions for dot product")
            return sum(a*b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a* other for a in self.components))
        else:
            raise TypeError("Unsupported operation")
    def __rmul__(self, scalar):
        return self*scalar
    def magnitude(self):
        return (sum(a**2 for a in self.components))** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot be a zero vector.")
        return Vector(*(a/mag for a in self.components))
    
    