from vector3 import Vector3


class Mesh:
    def __init__(self, vertices: list[Vector3], edges: list[tuple[int, int]]):
        self.vertices = vertices
        self.edges = edges
