import pygame

from rotation import rotate
from vector3 import Vector3


class Camera:
    SPEED = 0.01

    def __init__(self) -> None:
        self.position = Vector3(0, 0, -3)
        self.rotation = Vector3(0, 0, 0)

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.position.z += self.SPEED
        if keys[pygame.K_s]:
            self.position.z -= self.SPEED
        if keys[pygame.K_d]:
            self.position.x += self.SPEED
        if keys[pygame.K_a]:
            self.position.x -= self.SPEED
        if keys[pygame.K_e]:
            self.position.y += self.SPEED
        if keys[pygame.K_q]:
            self.position.y -= self.SPEED

    def transform_vertex(self, vertex: Vector3) -> Vector3:
        # apply camera rotation and position
        vertex = rotate(vertex, -1 * self.rotation)
        return vertex - self.position

    def transform_vertices(self, vertices: list[Vector3]) -> list[Vector3]:
        return [self.transform_vertex(vertex) for vertex in vertices]
