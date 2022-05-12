import pygame

class AntiBlur(pygame.sprite.Sprite):
    def __init__(self, obj):
        super(AntiBlur, self).__init__()
        width = object.surf.get_width() * 2
        height = object.surf.get_height() * 2
        self.surf = pygame.Surface([width, height])
        self.rect = self.surf.get_rect()

    def move(self, obj):
        

