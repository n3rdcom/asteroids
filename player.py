import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.last_shot_time = 0
        self.shots = shots

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt, direction_multiplier):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction_multiplier

    def shoot(self, shots):
        if pygame.time.get_ticks() - self.last_shot_time >= 300:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shots.add(shot)
            self.last_shot_time = pygame.time.get_ticks()

        
            

    def update(self, dt):
        keys = pygame.key.get_pressed()
        #Turning keys
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

        #Start at rest
        direction_multiplier = 0

        #Check for forward or backward movement
        if keys[pygame.K_w]:
            direction_multiplier = 1
        elif keys[pygame.K_s]:
            direction_multiplier = -1
        #Perform movement
        self.move(dt, direction_multiplier)

        #Shoot
        if keys[pygame.K_SPACE]:
            self.shoot(self.shots)


