from config import BLUE
from mesh import Mesh
from object3d import Object3D
from vector3 import Vector3


def create_cube() -> Object3D:
    vertices = [Vector3(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
    triangles = [
        (1, 2, 3),
        (1, 0, 2),
        (0, 1, 5),
        (4, 0, 5),
        (5, 6, 4),
        (7, 6, 5),
        (6, 3, 2),
        (7, 3, 6),
        (7, 5, 3),
        (3, 5, 1),
        (4, 2, 0),
        (6, 2, 4),
    ]
    return Object3D(Mesh(vertices, triangles), BLUE)
