import random


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


class ParticleSimulator:
    """Controls a single square."""

    def __init__(
        self,
        numbers: int = 10,
        x_range: tuple[int, int] = (0, 800),
        y_range: tuple[int, int] = (0, 600),
        radius_range: tuple[int, int] = (5, 40),
        velocity_range: tuple[int, int] = (1, 5),
        color: list[int] = [255, 0, 0],  # red
    ):
        particles = []
        for _ in range(numbers):
            particle = {}
            particle["x"] = random.randint(*x_range)
            particle["y"] = random.randint(*y_range)
            particle["radius"] = random.randint(*radius_range)
            particle["velocity"] = random.randint(*velocity_range)
            particle["color"] = color
            particles.append(particle)
        self.particles = particles

    def state(self):
        return self.particles

    def step(self):
        # update the simulation
        for particle in self.particles:
            particle["x"] += particle["velocity"]
            particle["y"] += particle["velocity"]
        # return the current state of the simulation
        return self.state()
