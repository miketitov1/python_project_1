import pygame

pygame.init()


class Button:
    """Класс кнопки"""

    def __init__(self, x_pos=200, y_pos=200, width=255, height=60, text='Sample text', text_color=(0, 0, 0),
                 bg_color=(255, 255, 255)):
        self.text = text
        self.font = pygame.font.SysFont('Georgia', 40, bold=True)
        self.button = pygame.Rect(x_pos, y_pos, width, height)
        self.text_color = text_color
        self.bg_color = bg_color

    def draw_button(self, screen):
        """Отрисовка кнопки"""
        surface = self.font.render(self.text, True, self.text_color)
        pygame.draw.rect(screen, self.bg_color, self.button)
        screen.blit(surface, (self.button.x + 5, self.button.y + 5))
