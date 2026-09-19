import math

from config import ORANGE
from mesh import Mesh
from object3d import Object3D
from vector3 import Vector3


def create_sphere() -> Object3D:
    rings = 16
    segments = 16
    vertices: list[Vector3] = []
    triangles: list[tuple[int, int, int]] = []

    # first create ring vertices
    for ring in range(1, rings):
        phi = math.pi / rings * ring
        ring_width = math.sin(phi)
        y = math.cos(phi)

        for segment in range(segments):
            angle = 2 * math.pi / segments * segment
            x = ring_width * math.cos(angle)
            z = ring_width * math.sin(angle)
            vertices.append(Vector3(x, y, z))

            # connect them with triangles
            ring_num = ring - 1
            current = ring_num * segments + segment
            next = (ring_num * segments) + (segment + 1) % segments
            below = (ring_num + 1) * segments + segment
            below_next = (ring_num + 1) * segments + (segment + 1) % segments

            if ring != rings - 1:
                triangles.append((current, below, next))
                triangles.append((next, below, below_next))

    # add top
    vertices.append(Vector3(0, 1, 0))
    for segment in range(segments):
        triangles.append((len(vertices) - 1, segment, (segment + 1) % segments))

    # add bottom
    vertices.append(Vector3(0, -1, 0))
    for segment in range(segments):
        triangles.append(
            (
                ((rings - 2) * segments + (segment + 1) % segments),
                (rings - 2) * segments + segment,
                len(vertices) - 1,
            )
        )

    return Object3D(Mesh(vertices, triangles), ORANGE)
