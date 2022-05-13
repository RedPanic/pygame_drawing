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


def reset_objects(objects):
    for item in objects:
        item.reset()


def clear_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.update()


def draw_objects(screen, objects: list):
    screen.fill((0, 0, 0))

    for item in objects:
        screen.blit(item.surf, item.rect)

    pygame.display.update()


def lock_objects(objects):
    for item in objects:
        item.lock()


def unlock_objects(objects):
    for item in objects:
        item.unlock()


def increase_velocity(obj, speed):
    obj.increase_velocity(speed)

def decrease_velocity(obj, speed):
    obj.decrease_velocity(speed)


def main():
    fps = 60
    running = True
    # SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    mode = 0
    first_ball_obj = Ball(64, 64, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 3,
                          SCREEN)
    second_ball_obj = Ball(64, 64, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 3,
                           SCREEN)
    bottom = SCREEN.get_height() - second_ball_obj.rect.height
    second_ball_obj.set_position(0, bottom)
    screen_objects = [first_ball_obj, second_ball_obj]

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
                    reset_objects(screen_objects)
                    clear_screen(SCREEN)
                if event.key == pygame.K_SPACE:
                    unlock_objects(screen_objects)
                if event.key == pygame.K_LCTRL:
                    lock_objects(screen_objects)
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_F10:
                    running = False
                if event.key == pygame.K_RIGHT:
                    increase_velocity(first_ball_obj, 5)
                    increase_velocity(second_ball_obj, 3)
                if event.key == pygame.K_LEFT:
                    decrease_velocity(first_ball_obj, 5)
                    decrease_velocity(second_ball_obj, 3)
                if event.key == pygame.K_INSERT:
                    clear_screen(SCREEN)

        move_ball(first_ball_obj, mode)
        move_ball(second_ball_obj, mode)
        draw_objects(SCREEN, screen_objects)


if __name__ == '__main__':
    pygame.init()
    main()
