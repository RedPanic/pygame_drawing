import pygame

class AntiBlur(pygame.sprite.Sprite):
    def __init__(self, obj):
        super(AntiBlur, self).__init__()
        width = obj.surf.get_width() * 2
        height = obj.surf.get_height() * 2
        self.surf = pygame.Surface([width, height])
        self.rect = self.surf.get_rect()

    def move(self, obj):
        self.rect.move_ip(obj.x_vec * obj.velocity, obj.y_vec * obj.velocity)

