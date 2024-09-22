class Particle:
    """A single particle object."""

    def __init__(
        self,
        init_x: int = 0,
        init_y: int = 0,
        velocity: int = 1,
        size: int = 100,
        color: list[int] = [255, 0, 0],  # red
    ):
        self.x = init_x
        self.y = init_y
        self.velocity = velocity
        self.size = size
        self.color = color
