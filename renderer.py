import pygame

from camera import Camera
from config import WIREFRAME_COLOUR
from object3d import Object3D
from projection import project_point, world_to_screen
from vector2 import Vector2


class Renderer:
    def __init__(self, screen: pygame.surface.Surface, camera: Camera) -> None:
        self.screen = screen
        self.camera = camera

    def render_object(self, object3d: Object3D) -> None:
        scale = 400.0
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

        # get the depth of each triangle
        triangles_to_draw: list[tuple[float, tuple[int, int, int]]] = []
        for triangle in object3d.mesh.triangles:
            i, j, k = triangle
            a = camera_vertices[i]
            b = camera_vertices[j]
            c = camera_vertices[k]

            # only draw triangles in in front of camera
            if a.z > 0 and b.z > 0 and c.z > 0:
                depth = (a.z + b.z + c.z) / 3
                triangles_to_draw.append((depth, triangle))

        # painters algorithm
        triangles_to_draw.sort(reverse=True)

        # use the vertex coordinates to draw the triangles first
        for depth, triangle in triangles_to_draw:
            i, j, k = triangle

            # get the world coordinates of the triangle vertices
            a = camera_vertices[i]
            b = camera_vertices[j]
            c = camera_vertices[k]

            # calculate the normal of the triangle
            edge1 = c - a
            edge2 = b - a
            normal = edge1.cross(edge2).normalize()

            # calculate the vector from the center of the triangle to the camera
            center = (a + b + c) / 3
            to_camera = (-1 * center).normalize()

            # only draw triangle of the normal is facing in similar direction as towards the camera
            if normal.dot(to_camera) >= 0:
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
