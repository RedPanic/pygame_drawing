import pygame


class AntiBlur(pygame.sprite.Sprite):
    def __init__(self, obj):
        super(AntiBlur, self).__init__()
        width = obj.surf.get_width() * 4
        height = obj.surf.get_height() * 4
        self.surf = pygame.Surface([width, height])
        self.rect = self.surf.get_rect()
        self.rect.x -= (obj.surf.get_width() // 2)
        self.rect.y -= (obj.surf.get_height() // 2)
        self.locked = True

    def reset(self):
        self.rect.x = 0
        self.rect.y = 0
        self.lock()

    def move(self, obj):
        if not self.locked:
            self.rect.move_ip((obj.x_vec * obj.velocity), (obj.y_vec * obj.velocity))

    def check_track(self):
        self.surf.fill((255, 255, 255))

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
