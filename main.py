import pygame

from config import BACKGROUND_COLOUR, MIN_HEIGHT, MIN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, TARGET_FPS


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Py3D")
    clock = pygame.time.Clock()

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

        clock.tick(TARGET_FPS)
        screen.fill(BACKGROUND_COLOUR)
        pygame.display.flip()


if __name__ == "__main__":
    main()
