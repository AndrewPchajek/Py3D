import pygame

from camera import Camera
from config import VERTEX_COLOUR, WIREFRAME_COLOUR
from mesh import Mesh
from projection import project_point, world_to_screen
from vector2 import Vector2


class Renderer:
    def __init__(self, screen: pygame.surface.Surface, camera: Camera) -> None:
        self.screen = screen
        self.camera = camera

    def render_mesh(self, mesh: Mesh) -> None:
        scale = 400.0
        radius = 5
        line_width = 1

        points: list[Vector2] = []
        width, height = self.screen.get_size()

        # first calculate the screen coordinates of each vertex
        for vertex in mesh.vertices:
            vertex = self.camera.world_to_camera(vertex)
            vertex2d = project_point(vertex)
            point = world_to_screen(vertex2d, width, height, scale)
            points.append(point)

        # use the vertex coordinates to draw the edges first
        for i, j in mesh.edges:
            pygame.draw.line(
                self.screen,
                WIREFRAME_COLOUR,
                (points[i].x, points[i].y),
                (points[j].x, points[j].y),
                line_width,
            )

        # draw the vertices
        for point in points:
            pygame.draw.circle(self.screen, VERTEX_COLOUR, (point.x, point.y), radius)
