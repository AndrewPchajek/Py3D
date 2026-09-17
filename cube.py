from mesh import Mesh
from vector3 import Vector3


def create_cube() -> Mesh:
    vertices = [Vector3(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
    edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7),
    ]
    return Mesh(vertices, edges)
