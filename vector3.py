from __future__ import annotations


class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Vector3) -> Vector3:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> Vector3:
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> Vector3:
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar: float) -> Vector3:
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def length(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self) -> Vector3:
        length = self.length()
        return self / length

    def dot(self, other: Vector3) -> float:
        return self.x * other.x + self.y * other.y + self.z + other.z

    def cross(self, other: Vector3) -> Vector3:
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def distance_to(self, other: Vector3) -> float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5
