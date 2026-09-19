from vector3 import Vector3


class Light:
    def __init__(self) -> None:
        self.position = Vector3(2, 2, -2)
        self.ambient = 0.4

    def calculate_colour(
        self, colour: tuple[int, int, int], dot_product: float, distance: float
    ) -> tuple[int, int, int]:

        directness = max(0, dot_product)
        strength = 1 / distance
        brightness = min(1, self.ambient + directness * strength)
        colour = (
            int(colour[0] * brightness),
            int(colour[1] * brightness),
            int(colour[2] * brightness),
        )
        return colour
