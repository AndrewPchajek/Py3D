import pygame

from camera import Camera
from light import Light
from object3d import Object3D
from projection import point_to_screen
from vector2 import Vector2


class Renderer:
    def __init__(self, screen: pygame.surface.Surface, camera: Camera, light: Light) -> None:
        self.screen = screen
        self.camera = camera
        self.light = light
        self.render_normal = False

    def toggle_normal(self) -> None:
        self.render_normal = not self.render_normal

    def render_object(self, object3d: Object3D) -> None:
        scale = 400.0

        width, height = self.screen.get_size()
        points: list[Vector2] = []

        light_cam_position = self.camera.transform_vertex(self.light.position)

        # object -> world space -> camera space
        world_vertices = object3d.get_transformed_vertices()
        camera_vertices = self.camera.transform_vertices(world_vertices)

        # camera space ->  screen coordinates
        for vertex in camera_vertices:
            point = point_to_screen(vertex, width, height, scale)
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

        # use the vertex coordinates to draw the triangles
        for _, triangle in triangles_to_draw:
            i, j, k = triangle

            # get the camera coordinates of the triangle vertices
            a = camera_vertices[i]
            b = camera_vertices[j]
            c = camera_vertices[k]

            # calculate the normal of the triangle
            edge1 = c - a
            edge2 = b - a
            normal = edge1.cross(edge2).normalize()

            # calculate the vector from the center of the triangle to the camera
            center = (a + b + c) / 3
            to_camera = (-1 * center).normalize()  # camera position is 0 in camera space
            to_light = (light_cam_position - center).normalize()

            # only draw triangle of the normal is facing in similar direction as towards the camera
            if normal.dot(to_camera) >= 0:
                colour = self.light.calculate_colour(
                    object3d.colour, normal.dot(to_light), light_cam_position.distance_to(center)
                )

                pygame.draw.polygon(
                    self.screen,
                    colour,
                    (
                        (points[i].x, points[i].y),
                        (points[j].x, points[j].y),
                        (points[k].x, points[k].y),
                    ),
                )

                if self.render_normal:
                    # render a normal line as the line from the center of each triangle outwards by the normal unit vector
                    center_pos = point_to_screen(center, width, height, scale)
                    normal_end_pos = point_to_screen(center + normal, width, height, scale)
                    pygame.draw.line(
                        self.screen,
                        (255, 165, 0),
                        (center_pos.x, center_pos.y),
                        (normal_end_pos.x, normal_end_pos.y),
                    )
