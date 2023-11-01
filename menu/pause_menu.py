import pygame
import sys

from menu.default_menu import DefaultMenu
from menu.button import Button

pygame.init()


class PauseMenu(DefaultMenu):
    """Логика меню паузы. Отвечает за взаимодействие с кнопками меню паузы"""

    def __init__(self, screen):
        super().__init__()

        self.main_screen = screen

        logo_font = pygame.font.SysFont('Georgia', 55, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Game paused', True, logo_color)

        bg_color = (0, 0, 0)
        self.pause_menu_window = pygame.Surface((2 * self.screen_width // 3, 2 * self.screen_height // 3))
        self.pause_menu_window.fill(bg_color)
        self.pause_menu_window.set_alpha(64)

        self.run = False
        self.resume = False
        self.restart = False
        self.go_to_main_menu = False

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (55, 55, 55)
        self.pressed_button_bg_color = (200, 200, 200)

        def pause_menu_resume():
            self.resume = True

        resume_button = Button(x_pos=self.screen_width // 3, y_pos=self.screen_height // 3,
                                    height=60, width=185, text='Resume',
                                    text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                    handle_event=pause_menu_resume)

        def pause_menu_restart():
            self.restart = True

        restart_button = Button(x_pos=self.screen_width // 3, y_pos=1.5 * self.screen_height // 3,
                                     height=60, width=170, text='Restart',
                                     text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                     handle_event=pause_menu_restart)

        def go_to_main_menu():
            self.go_to_main_menu = True

        go_to_main_menu_button = Button(x_pos=self.screen_width // 3, y_pos=2 * self.screen_height // 3,
                                             height=60, width=95, text='Exit',
                                             text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                             handle_event=go_to_main_menu)

        self.buttons_list.extend([resume_button, restart_button, go_to_main_menu_button])

    def pause_menu_events(self):
        """Класс меню паузы. Инициализирует всё меню паузы и обеспечивает его функционирование"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons_list:
                    if self.button_collision(button):
                        button.handle_event()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.resume = True

    def run_pause_menu(self):
        """Считывает действия пользователя и отрисовывает всё меню паузы"""
        self.pause_menu_events()
        self.update()
        self.draw_entities(self.main_screen)
        self.main_screen.blit(self.pause_menu_window, (self.screen_width // 6, self.screen_height // 6))
        self.main_screen.blit(self.logo_surface, (self.screen_width // 6 + 20, self.screen_height // 6 + 10))
        pygame.display.update()
