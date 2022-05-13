import pygame
import random
import time
from Objects.Ball import Ball
from Objects.AntiBlur import AntiBlur

WIDTH = 2560
HEIGHT = 1300


def move_ball(ball, mode):
    if mode == 1:
        ball.move()
    if mode == 2:
        ball.bounce()


def reset_ball(ball):
    ball.reset()


def clear_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.update()


def draw_objects(screen, objects: list):
    screen.fill((0, 0, 0))

    for item in objects:
        screen.blit(item.surf, item.rect)

    pygame.display.update()


def main():
    fps = 60
    running = True
    # SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    mode = 0
    ball_obj = Ball(64, 64, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 3, SCREEN)
    screen_objects = [ball_obj]

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 1
                if event.key == pygame.K_2:
                    mode = 2
                if event.key == pygame.K_0:
                    reset_ball(ball_obj)
                    clear_screen(SCREEN)
                if event.key == pygame.K_SPACE:
                    ball_obj.unlock()
                if event.key == pygame.K_LCTRL:
                    ball_obj.lock()
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_F10:
                    running = False
                if event.key == pygame.K_RIGHT:
                    ball_obj.increase_velocity(5)
                if event.key == pygame.K_LEFT:
                    ball_obj.deacrease_velocity(5)
                if event.key == pygame.K_INSERT:
                    clear_screen(SCREEN)

        move_ball(ball_obj, mode)
        draw_objects(SCREEN, screen_objects)


if __name__ == '__main__':
    pygame.init()
    main()
