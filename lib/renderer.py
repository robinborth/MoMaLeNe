import numpy as np


class SquareRenderer:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height

    def render(self, state: dict):
        # extract the state from the simulation
        x = state["x"]
        y = state["y"]
        size = state["size"]
        color = state["color"]

        # create the new image
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        img[x : x + size, y : y + size] = color

        return img


class ParticleRenderer:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height

    def render(self, state: dict):
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        for particle in state:
            # extract the state from the simulation
            x = particle["x"]
            y = particle["y"]
            size = particle["radius"]
            color = particle["color"]

            # create the new image
            img[x : x + size, y : y + size] = color

        return img
