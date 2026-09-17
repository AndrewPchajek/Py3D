from vector2 import Vector2
from vector3 import Vector3


def project_point(vector: Vector3, distance: float = 5.0) -> Vector2:
    x = vector.x / (vector.z + distance)
    y = vector.y / (vector.z + distance)
    return Vector2(x, y)


def world_to_screen(vector: Vector2, width: int, height: int, scale: float) -> Vector2:
    screen_x = width // 2 + vector.x * scale
    screen_y = height // 2 - vector.y * scale
    return Vector2(screen_x, screen_y)
