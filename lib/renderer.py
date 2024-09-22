import numpy as np
from lib.particle import Particle


class Renderer:
    """Maps all particles to an image."""

    def __init__(self, width: int = 600, height: int = 600):
        self.width = width
        self.height = height

    def transform_world_to_pixel(self, x: float, y: float):
        """Transforms a position in the world coordinate system to a pixel on the image."""
        u = (x + 1) * self.width / 2
        v = (y + 1) * self.height / 2
        return int(u), int(v)

    def transform_pixel_to_world(self, u: int, v: int):
        """Transforms a pixel on the image to a position in the world coordinate system."""
        x = (u * 2 / self.width) - 1
        y = (v * 2 / self.height) - 1
        return x, y

    def create_empty_image(self):
        return np.zeros((self.height, self.width, 3), dtype=np.uint8)  # (H, W, 3)

    def insert_rectangle(self, img, particle):
        # extract the state from the simulation
        u, v = self.transform_world_to_pixel(
            x=particle.x_position,
            y=particle.y_position,
        )
        radius = int(particle.radius * self.width / 2)
        color = particle.color
        # create the new image
        img[v - radius : v + radius, u - radius : u + radius] = color

    def insert_circle(self, img, particle):
        # extract the state from the simulation
        u, v = self.transform_world_to_pixel(
            x=particle.x_position,
            y=particle.y_position,
        )
        radius = int(particle.radius * self.width / 2)
        color = particle.color
        # create the new image
        for u_idx in range(u - radius, u + radius):
            for v_idx in range(v - radius, v + radius):
                x, y = self.transform_pixel_to_world(u=u_idx, v=v_idx)
                pixel_position = np.array([x, y])
                distance = np.linalg.norm(pixel_position - particle.position)
                if distance <= particle.radius:
                    img[v_idx, u_idx] = color

    def render(self, state: list[Particle]):
        """Renders an image from particle positions."""
        img = self.create_empty_image()
        for particle in state:
            self.insert_circle(img=img, particle=particle)
        return img
