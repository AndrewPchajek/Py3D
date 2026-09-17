from mesh import Mesh
from object3d import Object3D
from vector3 import Vector3


def create_cube() -> Object3D:
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
    return Object3D(Mesh(vertices, edges))
