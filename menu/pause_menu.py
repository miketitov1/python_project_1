import pygame
import sys

from menu.button import Button

pygame.init()


def pause_menu_events(pause_menu):
    """Считывает действия пользователя в меню паузы"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_menu.resume_button.button.collidepoint(event.pos):
                pause_menu.resume = True
            if pause_menu.restart_button.button.collidepoint(event.pos):
                pause_menu.restart = True
            if pause_menu.exit_button.button.collidepoint(event.pos):
                pause_menu.go_to_main_menu = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_menu.run = False
                pause_menu.resume = True


class Main:
    """Логика меню паузы. Отвечает за взаимодействие с кнопками меню паузы"""

    def __init__(self, screen_width, screen_height):
        self.run = False
        self.resume = False
        self.restart = False
        self.go_to_main_menu = False

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (55, 55, 55)
        self.pressed_button_bg_color = (200, 200, 200)
        self.resume_button = Button(x_pos=screen_width // 3, y_pos=screen_height // 3, height=60, width=185,
                                    text='Resume',
                                    text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)
        self.restart_button = Button(x_pos=screen_width // 3, y_pos=1.5 * screen_height // 3, height=60, width=170,
                                     text='Restart',
                                     text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)
        self.exit_button = Button(x_pos=screen_width // 3, y_pos=2 * screen_height // 3, height=60, width=95,
                                  text='Exit',
                                  text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)

    def update(self):
        """Проверка наведения курсора мыши на кнопки меню паузы"""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.button_collision(self.resume_button, mouse_pos_x, mouse_pos_y)
        self.button_collision(self.restart_button, mouse_pos_x, mouse_pos_y)
        self.button_collision(self.exit_button, mouse_pos_x, mouse_pos_y)

    def draw_entities(self, screen):
        """Отрисовка кнопок меню паузы"""
        self.resume_button.draw_button(screen)
        self.restart_button.draw_button(screen)
        self.exit_button.draw_button(screen)

    def button_collision(self, button, mouse_pos_x, mouse_pos_y):
        """Проверка наведения мыши на одну конкретную кнопку меню паузы"""
        if button.button.collidepoint(mouse_pos_x, mouse_pos_y):
            button.bg_color = self.pressed_button_bg_color
            return
        else:
            button.bg_color = self.unpressed_button_bg_color


class PauseMenu:
    """Класс меню паузы. По сути инициализирует всё меню паузы и обеспечивает его функционирование"""

    def __init__(self, screen):
        self.game_screen = screen
        self.screen_height = 640
        self.screen_width = 640

        logo_font = pygame.font.SysFont('Georgia', 55, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Game paused', True, logo_color)

        bg_color = (0, 0, 0)
        self.pause_menu_window = pygame.Surface((2 * self.screen_width // 3, 2 * self.screen_height // 3))
        self.pause_menu_window.fill(bg_color)
        self.pause_menu_window.set_alpha(64)

        self.pause_menu = Main(self.screen_width, self.screen_height)

    def run_pause_menu(self):
        """Считывает действия пользователя и отрисовывает всё меню паузы"""
        pause_menu_events(self.pause_menu)
        self.pause_menu.update()
        self.pause_menu.draw_entities(self.game_screen)

        self.game_screen.blit(self.pause_menu_window, (self.screen_width // 6, self.screen_height // 6))
        self.game_screen.blit(self.logo_surface, (self.screen_width // 6 + 20, self.screen_height // 6 + 10))

        pygame.display.update()
