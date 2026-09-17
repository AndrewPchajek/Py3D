import pygame

from camera import Camera
from config import VERTEX_COLOUR, WIREFRAME_COLOUR
from object3d import Object3D
from projection import project_point, world_to_screen
from vector2 import Vector2


class Renderer:
    def __init__(self, screen: pygame.surface.Surface, camera: Camera) -> None:
        self.screen = screen
        self.camera = camera

    def render_object(self, object3d: Object3D) -> None:
        scale = 400.0
        radius = 5
        line_width = 1

        width, height = self.screen.get_size()
        points: list[Vector2] = []

        # object -> world space -> camera space
        world_vertices = object3d.get_transformed_vertices()
        camera_vertices = self.camera.transform_vertices(world_vertices)

        # camera space -> 2d space -> screen coordinates
        for vertex in camera_vertices:
            point = project_point(vertex)
            point = world_to_screen(point, width, height, scale)
            points.append(point)

        # use the vertex coordinates to draw the triangles first
        for i, j, k in object3d.mesh.triangles:
            pygame.draw.polygon(
                self.screen,
                WIREFRAME_COLOUR,
                (
                    (points[i].x, points[i].y),
                    (points[j].x, points[j].y),
                    (points[k].x, points[k].y),
                ),
                line_width,
            )

        # draw the vertices
        for point in points:
            pygame.draw.circle(self.screen, VERTEX_COLOUR, (point.x, point.y), radius)
