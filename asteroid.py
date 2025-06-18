import pygame
import random
from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, vel1)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, vel2)
            Asteroid.add(new_asteroid1)
            Asteroid.add(new_asteroid2)

