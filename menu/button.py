import pygame
import sys

pygame.init()


class Button:
    """Класс кнопки"""

    def __init__(self, x_pos=200, y_pos=200, width=255, height=60, text='Sample text', text_color=(0, 0, 0),
                 bg_color=(255, 255, 255), handle_event=None):
        self.text = text
        self.font = pygame.font.SysFont('Georgia', 40, bold=True)
        self.button_rect = pygame.Rect(x_pos, y_pos, width, height)
        self.text_color = text_color
        self.bg_color = bg_color
        if handle_event:
            self.handle_event = handle_event

    def draw_button(self, screen):
        """Отрисовка кнопки"""
        surface = self.font.render(self.text, True, self.text_color)
        pygame.draw.rect(screen, self.bg_color, self.button_rect)
        screen.blit(surface, (self.button_rect.x + 5, self.button_rect.y + 5))

    def handle_event(self):
        pass
