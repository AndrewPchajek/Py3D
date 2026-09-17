import math

from vector3 import Vector3


def rotate_x(vector: Vector3, angle: float) -> Vector3:
    x = vector.x
    y = vector.y * math.cos(angle) - vector.z * math.sin(angle)
    z = vector.y * math.sin(angle) + vector.z * math.cos(angle)
    return Vector3(x, y, z)


def rotate_y(vector: Vector3, angle: float) -> Vector3:
    x = vector.x * math.cos(angle) + vector.z * math.sin(angle)
    y = vector.y
    z = -1 * vector.x * math.sin(angle) + vector.z * math.cos(angle)
    return Vector3(x, y, z)


def rotate_z(vector: Vector3, angle: float) -> Vector3:
    x = vector.x * math.cos(angle) - vector.y * math.sin(angle)
    y = vector.x * math.sin(angle) + vector.y * math.cos(angle)
    z = vector.z
    return Vector3(x, y, z)
