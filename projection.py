from vector2 import Vector2
from vector3 import Vector3


def point_to_screen(vector: Vector3, width: int, height: int, scale: float) -> Vector2:
    point = project_point(vector)
    return adjust_to_screen(point, width, height, scale)


def project_point(vector: Vector3) -> Vector2:
    x = vector.x / (vector.z)
    y = vector.y / (vector.z)
    return Vector2(x, y)


def adjust_to_screen(vector: Vector2, width: int, height: int, scale: float) -> Vector2:
    screen_x = width // 2 + vector.x * scale
    screen_y = height // 2 - vector.y * scale
    return Vector2(screen_x, screen_y)
