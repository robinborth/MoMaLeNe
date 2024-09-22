import numpy as np
from dataclasses import dataclass


class Particle:
    """A single particle object. Lives in the world coordinate system between -1 and 1."""

    def __init__(
        self,
        velocity: np.ndarray | None = None,  # vector
        position: np.ndarray | None = None,  # point
        radius: float = 2e-02,
        color: list[int] = [255, 0, 0],  # red
    ):
        self.velocity = velocity
        if self.velocity is None:
            self.velocity = np.zeros(2)
        self.position = position
        if self.position is None:
            self.position = np.zeros(2)
        self.radius = radius
        self.color = color
        self.mass = 1

    @property
    def x_position(self):
        return self.position[0]

    @property
    def y_position(self):
        return self.position[1]

    def set_x_position(self, x: float):
        self.position[0] = x

    def set_y_position(self, y: float):
        self.position[1] = y

    @property
    def x_velocity(self):
        return self.velocity[0]

    @property
    def y_velocity(self):
        return self.velocity[1]

    def set_x_velocity(self, x: float):
        self.velocity[0] = x

    def set_y_velocity(self, y: float):
        self.velocity[1] = y
