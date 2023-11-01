import pygame
import random
from pygame.math import Vector2

pygame.init()


class Fruit:
    """Класс фрукта"""

    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        x_pos = random.randint(0, cell_number - 1)
        y_pos = random.randint(0, cell_number - 1)
        self.pos = Vector2(x_pos, y_pos)
        self.color = (126, 166, 114)

    def draw_fruit(self, screen):
        """Отрисовка фрукта"""
        x_pos = self.pos.x * self.cell_size
        y_pos = self.pos.y * self.cell_size
        fruit_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, self.color, fruit_rect)

    def respawn(self):
        """Перезагрузка фрукта. Перемещает фрукт в случайное место на карте"""
        self.pos.x = random.randint(0, self.cell_number - 1)
        self.pos.y = random.randint(0, self.cell_number - 1)
