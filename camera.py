import pygame

from vector3 import Vector3


class Camera:
    SPEED = 0.01

    def __init__(self) -> None:
        self.position = Vector3(0, 0, 0)

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

    def world_to_camera(self, point: Vector3) -> Vector3:
        return point - self.position
