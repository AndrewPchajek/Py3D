from mesh import Mesh
from rotation import rotate
from vector3 import Vector3


class Object3D:
    def __init__(self, mesh: Mesh) -> None:
        self.mesh = mesh
        self.position= Vector3(0, 0, 0)
        self.rotation= Vector3(0, 0, 0)

    def get_transformed_vertices(self) -> list[Vector3]:
        transformed_vertices: list[Vector3] = []

        for vertex in self.mesh.vertices:
            # apply object rotation and position to each vertex
            vertex = rotate(vertex, self.rotation)
            vertex = vertex + self.position
            transformed_vertices.append(vertex)

        return transformed_vertices
