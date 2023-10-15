import pygame

class Inimigos:
    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(self.x, self.y)
        self.rect = tipo[0].get_rect()

    def seguir(self, destino):
        if self.pos[0] < destino[0]:
            self.pos[0] += 1
        if self.pos[0] > destino[0]:
            self.pos[0] -= 1
        if self.pos[1] < destino[1]:
            self.pos[1] += 1
        if self.pos[1] > destino[1]:
            self.pos[1] -= 1
        
        self.rect.topleft = self.pos