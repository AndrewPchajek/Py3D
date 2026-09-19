from config import RED
from mesh import Mesh
from object3d import Object3D
from vector3 import Vector3


def create_pyramid() -> Object3D:
    vertices = [
        Vector3(-1, -1, -1),
        Vector3(-1, -1, 1),
        Vector3(1, -1, 1),
        Vector3(1, -1, -1),
        Vector3(0, 1, 0),
    ]
    triangles = [(3, 0, 1), (2, 3, 1), (3, 4, 0), (0, 4, 1), (1, 4, 2), (2, 4, 3)]
    return Object3D(Mesh(vertices, triangles), RED)
