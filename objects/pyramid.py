from mesh import Mesh
from vector3 import Vector3


def create_pyramid() -> Mesh:
    vertices = [
        Vector3(-1, 0, -1),
        Vector3(-1, 0, 1),
        Vector3(1, 0, 1),
        Vector3(1, 0, -1),
        Vector3(0, 2, 0),
    ]
    triangles = [(3, 0, 1), (2, 3, 1), (3, 4, 0), (0, 4, 1), (1, 4, 2), (2, 4, 3)]
    return Mesh(vertices, triangles)
