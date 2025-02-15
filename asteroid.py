import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        neg_vector = self.velocity.rotate(-random_angle)
        pos_vector = self.velocity.rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        neg_Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_Asteroid.velocity = neg_vector * 1.2
        pos_Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        pos_Asteroid.velocity = pos_vector * 1.2

