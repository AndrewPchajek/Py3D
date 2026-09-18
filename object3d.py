import pygame

from objects.cube import create_cube
from objects.pyramid import create_pyramid
from rotation import rotate
from vector3 import Vector3


class Object3D:
    SPEED = 0.01

    def __init__(self) -> None:
        self.mesh = create_cube()
        self.reset_position_and_rotation()

    def reset_position_and_rotation(self):
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.mesh = create_cube()
            self.reset_position_and_rotation()
        if keys[pygame.K_2]:
            self.mesh = create_pyramid()
            self.reset_position_and_rotation()

        if keys[pygame.K_UP]:
            self.rotation.x += self.SPEED
        if keys[pygame.K_DOWN]:
            self.rotation.x -= self.SPEED
        if keys[pygame.K_LEFT]:
            self.rotation.y += self.SPEED
        if keys[pygame.K_RIGHT]:
            self.rotation.y -= self.SPEED

    def get_transformed_vertices(self) -> list[Vector3]:
        transformed_vertices: list[Vector3] = []

        for vertex in self.mesh.vertices:
            # apply object rotation and position to each vertex
            vertex = rotate(vertex, self.rotation)
            vertex = vertex + self.position
            transformed_vertices.append(vertex)

        return transformed_vertices
