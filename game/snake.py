import pygame
from pygame.math import Vector2

pygame.init()


class Snake:
    """Класс змеи"""

    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.body = [Vector2(cell_number // 2, cell_number // 2),
                     Vector2(cell_number // 2 - 1, cell_number // 2),
                     Vector2(cell_number // 2 - 2, cell_number // 2)]
        self.direction = Vector2(1, 0)
        self.color = (183, 111, 122)
        self.growth_indicator = False

    def update_snake(self):
        """Обновление положения змеи"""
        if self.growth_indicator:
            temp_body = self.body
            temp_body.insert(0, temp_body[0] + self.direction)
            self.body = temp_body
            self.growth_indicator = False
        else:
            temp_body = self.body[:-1]
            temp_body.insert(0, temp_body[0] + self.direction)
            self.body = temp_body

    def draw_snake(self, screen):
        """Отрисовка змеи"""
        for segment in self.body:
            x_pos = segment.x * self.cell_size
            y_pos = segment.y * self.cell_size
            segment_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, self.color, segment_rect)

    def grow(self):
        """Рост змеи"""
        self.growth_indicator = True

    def respawn(self):
        """Перезагрузка змеи. Возвращает змею в исходное положение и удаляет все сегменты кроме начальных"""
        self.body = [Vector2(self.cell_number // 2, self.cell_number // 2),
                     Vector2(self.cell_number // 2 - 1, self.cell_number // 2),
                     Vector2(self.cell_number // 2 - 2, self.cell_number // 2)]
        self.direction = Vector2(1, 0)
