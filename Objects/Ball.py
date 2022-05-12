import random
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, color, velocity, screen):
        super(Ball, self).__init__()
        self.surf = pygame.Surface([width, height])
        self.rect = self.surf.get_rect()
        self.draw_ball(color)
        self.velocity = velocity
        self.locked = True
        self.screen = screen
        self.x_vec = 1
        self.y_vec = 1

    def draw_ball(self, color):
        pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2),
                           self.surf.get_width() // 2)

    def move(self):
        if self.locked:
            return
        if self.rect.x >= self.screen.get_width():
            self.rect.x = 0
            self.rect.move_ip(0, self.velocity * 3)
            if self.rect.y >= self.screen.get_height():
                self.draw_ball((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
                self.rect.y = 0
        self.rect.move_ip(self.velocity, 0)

    def bounce(self):
        if self.locked:
            return

        if (self.rect.x + self.rect.width) >= self.screen.get_width() or self.rect.x < 0:
            # Ball is reaching right side
            self.x_vec = -self.x_vec
        if (self.rect.y + self.rect.height) >= self.screen.get_height() or self.rect.y < 0:
            # Ball is reaching down side
            self.y_vec = -self.y_vec

        self.rect.move_ip(self.x_vec * self.velocity, self.y_vec * self.velocity)

    def unlock_ball(self):
        self.locked = False

    def lock_ball(self):
        self.locked = True

    def increase_velocity(self, value):
        self.velocity += value

    def deacrease_velocity(self, value):
        self.velocity -= value
