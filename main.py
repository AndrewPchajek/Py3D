import pygame

from camera import Camera
from config import BACKGROUND_COLOUR, MIN_HEIGHT, MIN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, TARGET_FPS
from object3d import Object3D
from renderer import Renderer


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Py3D")
    clock = pygame.time.Clock()

    camera = Camera()
    renderer = Renderer(screen, camera)
    object3d = Object3D()

    while True:
        for event in pygame.event.get():
            # if the user hits the x button quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # let the user resize the window
            elif event.type == pygame.VIDEORESIZE:
                # make the size at least the minimum
                width, height = event.size

                # only update the window if needed
                if width < MIN_WIDTH:
                    screen = pygame.display.set_mode((MIN_WIDTH, height), pygame.RESIZABLE)
                if height < MIN_HEIGHT:
                    screen = pygame.display.set_mode((width, MIN_HEIGHT), pygame.RESIZABLE)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    renderer.toggle_normal()

        camera.update()
        object3d.update()

        screen.fill(BACKGROUND_COLOUR)
        renderer.render_object(object3d)
        pygame.display.flip()

        clock.tick(TARGET_FPS)


if __name__ == "__main__":
    main()
