import pygame
import sys

pygame.init()


class DefaultMenu:
    """Класс меню. Инициализирует всё меню и обеспечивает его функционирование"""

    def __init__(self, screen_height=640, screen_width=640, game_name="Snake", screen_color=(255, 255, 255)):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(game_name)
        self.screen_color = screen_color
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (110, 110, 110)
        self.pressed_button_bg_color = (180, 180, 180)
        self.buttons_list = []
        self.input_box_list = []

    def update(self):
        """Проверка наведения курсора мыши на кнопки"""
        for button in self.buttons_list:
            if self.button_collision(button):
                button.bg_color = self.pressed_button_bg_color
            else:
                button.bg_color = self.unpressed_button_bg_color
        for input_box in self.input_box_list:
            input_box.update()

    def draw_entities(self, screen):
        """Отрисовка кнопок"""
        for button in self.buttons_list:
            button.draw_button(screen)
        for input_box in self.input_box_list:
            input_box.draw(screen)

    def button_collision(self, button):
        """Проверка наведения мыши на одну конкретную кнопку"""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        return button.button_rect.collidepoint(mouse_pos_x, mouse_pos_y)

    def menu_events(self):
        """Считывает действия пользователя в меню"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons_list:
                    if self.button_collision(button):
                        button.handle_event()

    def run_menu(self):
        """Считывает действия пользователя и отрисовывает всё меню"""
        self.menu_events()
        self.update()
        self.screen.fill(self.screen_color)
        self.draw_entities(self.screen)
        pygame.display.update()
        self.clock.tick(self.FPS)
