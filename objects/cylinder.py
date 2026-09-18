import math

from mesh import Mesh
from vector3 import Vector3


def create_cylinder() -> Mesh:
    segments = 16
    vertices: list[Vector3] = []
    triangles: list[tuple[int, int, int]] = []

    # add the triangles for the sides of the cylinder
    for i in range(segments):
        angle = 2 * math.pi / segments * i
        x = math.cos(angle)
        z = math.sin(angle)

        vertices.append(Vector3(x, 1, z))
        vertices.append(Vector3(x, -1, z))

        next_i = (i + 1) % segments
        triangles.append((2 * i, 2 * i + 1, 2 * next_i))
        triangles.append((2 * next_i, 2 * i + 1, 2 * next_i + 1))

    # add a vertex in the center of both circles
    vertices.append(Vector3(0, 1, 0))
    vertices.append(Vector3(0, -1, 0))

    # add the triangles for the top and bottom of the cylinder
    for i in range(segments):
        next_i = (i + 1) % segments
        top_center_index = len(vertices) - 2
        bottom_center_index = len(vertices) - 1
        triangles.append((top_center_index, 2 * i, 2 * next_i))
        triangles.append((bottom_center_index, 2 * next_i + 1, 2 * i + 1))

    return Mesh(vertices, triangles)
