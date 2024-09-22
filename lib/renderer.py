import numpy as np
from lib.particle import Particle


class Renderer:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height

    def render(self, state: list[Particle]):
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        for particle in state:
            # extract the state from the simulation
            x = particle.x
            y = particle.y
            size = particle.size
            color = particle.color

            # create the new image
            img[x : x + size, y : y + size] = color

        return img
