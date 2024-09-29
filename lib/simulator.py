from lib.particle import Particle
import numpy as np
import random


class Simulator:
    """Owns all particles in the world coordinate system. Simulates their movement.

    @num_particles: Number of particles simulated.
    @gravity: Value by which to increase a particle's velocity along the y-axis each step.
    @border: The border of the coordinate system we are simulating in.
    @damping_factor: The friction to lower the velocity of a particle on each change in direction.
    """

    def __init__(
        self,
        num_particles: int = 64,
        gravity: float = 3e-04,
        damping_factor: float = 0.7,
    ):
        self.border = 1.0
        self.particles = self.generate_particle_grid(num_particles=num_particles)
        self.gravity = np.array([0.0, gravity])
        self.damping_factor = damping_factor

    def generate_particle_grid(self, num_particles: int):
        # Create 10 values from -0.5 to 0.5 for both x and y axes
        x = np.linspace(-0.5, 0.5, int(np.sqrt(num_particles)))
        y = np.linspace(-0.5, 0.5, int(np.sqrt(num_particles)))
        # Create the 2D grid
        X, Y = np.meshgrid(x, y)
        # Stack the coordinates if needed as a grid of points
        grid = np.stack([X, Y], axis=-1)

        particles = []
        for position in grid.reshape(-1, 2):
            particle = Particle(position=position)
            particle.set_x_velocity(random.random() * 1e-02)
            particles.append(particle)
        return particles

    def step(self):
        def border_collision(particle: Particle):
            # Keep particle within lower border
            if particle.y_position >= (border := self.border - particle.radius):
                particle.set_y_position(border)
                particle.set_y_velocity(-particle.y_velocity * self.damping_factor)
                particle.set_x_velocity(particle.x_velocity * self.damping_factor)
            # Keep particle within upper border
            elif particle.y_position <= (border := -self.border + particle.radius):
                particle.set_y_position(border)
                particle.set_y_velocity(-particle.y_velocity * self.damping_factor)
            # Keep particle within left border
            if particle.x_position >= (border := self.border - particle.radius):
                particle.set_x_position(border)
                particle.set_x_velocity(-particle.x_velocity * self.damping_factor)
            # Keep particle within right border
            elif particle.x_position <= (border := -self.border + particle.radius):
                particle.set_x_position(border)
                particle.set_x_velocity(-particle.x_velocity * self.damping_factor)

        # Update the simulation
        for particle in self.particles:
            # Apply gravity
            particle.velocity += self.gravity
            # Update particle
            particle.position += particle.velocity
            # Check particle is within the border
            border_collision(particle=particle)

        # Return the current state of the simulation
        return self.particles
