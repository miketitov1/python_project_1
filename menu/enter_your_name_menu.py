import pygame
import sys

from button import Button
from input_box import Inputbox

pygame.init()


def enter_your_name_menu_events(enter_your_name_menu, input_box, new_score):
    """Считывает действия пользователя в меню ввода имени"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        input_box.handle_event(event, new_score)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if enter_your_name_menu.restart_button.button.collidepoint(event.pos):
                enter_your_name_menu.restart = True
            if enter_your_name_menu.exit_button.button.collidepoint(event.pos):
                enter_your_name_menu.go_to_main_menu = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_ESCAPE:
                enter_your_name_menu.go_to_main_menu = True


class Main:
    """Логика меню ввода имени. Отвечает за взаимодействие с кнопками"""

    def __init__(self, screen_width, screen_height):
        self.run = False
        self.restart = False
        self.go_to_main_menu = False

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (55, 55, 55)
        self.pressed_button_bg_color = (200, 200, 200)
        self.restart_button = Button(x_pos=screen_width // 3, y_pos=1.5 * screen_height // 3, width=170, height=60,
                                     text='Restart', text_color=self.button_text_color,
                                     bg_color=self.unpressed_button_bg_color)
        self.exit_button = Button(x_pos=screen_width // 3, y_pos=2 * screen_height // 3, width=95, height=60,
                                  text='Exit',
                                  text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)

        self.input_box = Inputbox(screen_width // 3, screen_height // 3, 140, 60)

    def update(self):
        """Проверка наведения курсора мыши на кнопки"""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.input_box.update()
        self.button_collision(self.restart_button, mouse_pos_x, mouse_pos_y)
        self.button_collision(self.exit_button, mouse_pos_x, mouse_pos_y)

    def draw_entities(self, screen):
        """Отрисовка кнопок"""
        self.input_box.draw(screen)
        self.restart_button.draw_button(screen)
        self.exit_button.draw_button(screen)

    def button_collision(self, button, mouse_pos_x, mouse_pos_y):
        """Проверка наведения мыши на одну конкретную кнопку"""
        if button.button.collidepoint(mouse_pos_x, mouse_pos_y):
            button.bg_color = self.pressed_button_bg_color
            return
        else:
            button.bg_color = self.unpressed_button_bg_color


class EnterYourNameMenu:
    """Класс меню ввода имени. Инициализирует всё меню ввода имени и обеспечивает его функционирование"""

    def __init__(self, screen):
        self.game_screen = screen
        self.screen_height = 640
        self.screen_width = 640

        logo_font = pygame.font.SysFont('Georgia', 43, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Enter your name:', True, logo_color)

        bg_color = (0, 0, 0)
        self.enter_your_name_menu_window = pygame.Surface((2 * self.screen_width // 3, 2 * self.screen_height // 3))
        self.enter_your_name_menu_window.fill(bg_color)
        self.enter_your_name_menu_window.set_alpha(64)

        self.enter_your_name_menu = Main(self.screen_width, self.screen_height)

    def run_enter_your_name_menu(self, new_score):
        """Считывает действия пользователя и отрисовывает всё меню ввода имени"""
        enter_your_name_menu_events(self.enter_your_name_menu, self.enter_your_name_menu.input_box, new_score)
        self.enter_your_name_menu.update()
        self.enter_your_name_menu.draw_entities(self.game_screen)

        self.game_screen.blit(self.enter_your_name_menu_window, (self.screen_width // 6, self.screen_height // 6))
        self.game_screen.blit(self.logo_surface, (self.screen_width // 6 + 20, self.screen_height // 6 + 10))

        pygame.display.update()
