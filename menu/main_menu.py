import pygame
import sys

from button import Button

pygame.init()


def main_menu_events(main_menu):
    """Считывает действия пользователя в главном меню"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.exit_button.button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if main_menu.endless_mode_button.button.collidepoint(event.pos):
                main_menu.go_to_endless_mode = True
            if main_menu.records_button.button.collidepoint(event.pos):
                main_menu.go_to_records_menu = True


class Main:
    """Логика главного меню. Отвечает за взаимодействие с кнопками"""

    def __init__(self, screen_width, screen_height):
        self.run = True
        self.go_to_story_mode = False
        self.go_to_endless_mode = False
        self.go_to_records_menu = False

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (110, 110, 110)
        self.pressed_button_bg_color = (180, 180, 180)
        self.endless_mode_button = Button(x_pos=screen_width // 3, y_pos=screen_height // 3, height=60, width=105,
                                          text='Play',
                                          text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)
        self.records_button = Button(x_pos=screen_width // 3, y_pos= screen_height // 2, height=60, width=180,
                                     text='Records',
                                     text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)
        self.exit_button = Button(x_pos=screen_width // 3, y_pos= 2 * screen_height // 3, height=60, width=95,
                                  text='Exit',
                                  text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)

    def update(self):
        """Проверка наведения курсора мыши на кнопки"""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.button_collision(self.endless_mode_button, mouse_pos_x, mouse_pos_y)
        self.button_collision(self.records_button, mouse_pos_x, mouse_pos_y)
        self.button_collision(self.exit_button, mouse_pos_x, mouse_pos_y)

    def draw_entities(self, screen):
        """Отрисовка кнопок"""
        self.endless_mode_button.draw_button(screen)
        self.records_button.draw_button(screen)
        self.exit_button.draw_button(screen)

    def button_collision(self, button, mouse_pos_x, mouse_pos_y):
        """Проверка наведения мыши на одну конкретную кнопку"""
        if button.button.collidepoint(mouse_pos_x, mouse_pos_y):
            button.bg_color = self.pressed_button_bg_color
            return
        else:
            button.bg_color = self.unpressed_button_bg_color


class MainMenu:
    """Класс главного меню. Инициализирует всё главное меню и обеспечивает его функционирование"""

    def __init__(self):
        self.screen_height = 640
        self.screen_width = 640
        self.main_menu_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake")
        self.screen_color = (114, 77, 163)

        logo_font = pygame.font.SysFont('Georgia', 80, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Snake', True, logo_color)

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.main_menu = Main(self.screen_width, self.screen_height)

    def run_main_menu(self):
        """Считывает действия пользователя и отрисовывает всё главное меню"""
        main_menu_events(self.main_menu)
        self.main_menu.update()
        self.main_menu_screen.fill(self.screen_color)
        self.main_menu.draw_entities(self.main_menu_screen)
        self.main_menu_screen.blit(self.logo_surface, (self.screen_width // 3, self.screen_height // 12))
        pygame.display.update()
        self.clock.tick(self.FPS)
