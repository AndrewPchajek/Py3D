from vector3 import Vector3


class Mesh:
    def __init__(self, vertices: list[Vector3], triangles: list[tuple[int, int, int]]):
        self.vertices = vertices
        self.triangles = triangles
