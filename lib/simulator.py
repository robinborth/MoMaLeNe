import random
from lib.particle import Particle


class Simulator:
    """Owns all particles in the coordinate system. Simulates their movement."""

    def __init__(
        self,
        num_particles: int = 1,
        x_range: tuple[int, int] = (0, 800),
        y_range: tuple[int, int] = (0, 600),
        radius_range: tuple[int, int] = (5, 40),
        velocity_range: tuple[int, int] = (1, 5),
        color: list[int] = [255, 0, 0],  # red
    ):
        self.particles = [
            Particle(
                random.randint(*x_range),
                random.randint(*y_range),
                random.randint(*velocity_range),
                random.randint(*radius_range),
                color,
            )
            for _ in range(num_particles)
        ]

    def step(self):
        # update the simulation
        for particle in self.particles:
            particle.x += particle.velocity
            particle.y += particle.velocity
        # return the current state of the simulation
        return self.particles
