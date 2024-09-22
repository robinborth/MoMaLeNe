class SquareSimulator:
    """Controls a single square."""

    def __init__(
        self,
        init_x: int = 0,
        init_y: int = 0,
        speed: int = 1,
        size: int = 100,
        color: list[int] = [255, 0, 0],  # red
    ):
        self.x = init_x
        self.y = init_y
        self.size = size
        self.color = color
        self.speed = speed

    def state(self):
        return {"x": self.x, "y": self.y, "size": self.size, "color": self.color}

    def step(self):
        # update the simulation
        self.x += self.speed
        self.y += self.speed
        # return the current state of the simulation
        return self.state()
