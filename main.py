import pygame
import random
from Objects.Ball import Ball

WIDTH = 2560
HEIGHT = 1300


def move_ball(ball, mode):
    if mode == 1:
        ball.move()
    if mode == 2:
        ball.bounce()


def reset_ball(ball):
    ball.rect.x = 0
    ball.rect.y = 0
    ball.lock_ball()


def clear_screen(screen):
    screen.fill((0, 0, 0))


def main():
    FPS = 60
    running = True
    # SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    mode = 0
    ball_obj = Ball(64, 64, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 3, SCREEN)
    anti_blur_rect = ball_obj.rect
    on_screen_objects = [ball_obj]
    SCREEN.blit(ball_obj.surf, ball_obj.rect)

    while running:
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
                    ball_obj.unlock_ball()
                if event.key == pygame.K_LCTRL:
                    ball_obj.lock_ball()
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_F10:
                    running = False
                if event.key == pygame.K_RIGHT:
                    ball_obj.increase_velocity(20)
                if event.key == pygame.K_LEFT:
                    ball_obj.deacrease_velocity(20)
                if event.key == pygame.K_INSERT:
                    clear_screen(SCREEN)

        SCREEN.fill((0, 0, 0))
        move_ball(ball_obj, mode)

        # SCREEN.blit(SCREEN, SCREEN.get_rect())
        pygame.display.update()
        SCREEN.blit(ball_obj.surf, ball_obj.rect)
        pygame.display.update(on_screen_objects)
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
