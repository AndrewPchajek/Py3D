from mesh import Mesh
from object3d import Object3D
from vector3 import Vector3


def create_cube() -> Object3D:
    vertices = [Vector3(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
    triangles = [
        (0, 1, 2),
        (1, 2, 3),
        (0, 1, 5),
        (0, 5, 4),
        (0, 2, 6),
        (0, 6, 4),
        (5, 4, 6),
        (5, 7, 6),
        (2, 6, 3),
        (3, 6, 7),
        (1, 3, 5),
        (3, 5, 7),
    ]
    return Object3D(Mesh(vertices, triangles))
