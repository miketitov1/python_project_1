import pygame
import sys

from menu.default_menu import DefaultMenu
from menu.button import Button
from menu.input_box import Inputbox

pygame.init()


class EnterYourNameMenu(DefaultMenu):
    """Класс меню ввода имени. Инициализирует всё меню ввода имени и обеспечивает его функционирование"""

    def __init__(self, screen):
        super().__init__()
        self.main_screen = screen

        logo_font = pygame.font.SysFont('Georgia', 43, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Enter your name:', True, logo_color)

        bg_color = (0, 0, 0)
        self.enter_your_name_menu_window = pygame.Surface((2 * self.screen_width // 3, 2 * self.screen_height // 3))
        self.enter_your_name_menu_window.fill(bg_color)
        self.enter_your_name_menu_window.set_alpha(64)

        self.run = False
        self.restart = False
        self.go_to_main_menu = False

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (55, 55, 55)
        self.pressed_button_bg_color = (200, 200, 200)

        def enter_your_name_menu_restart():
            self.restart = True

        restart_button = Button(x_pos=self.screen_width // 3, y_pos=1.5 * self.screen_height // 3, width=170, height=60,
                                text='Restart', text_color=self.button_text_color,
                                bg_color=self.unpressed_button_bg_color,
                                handle_event=enter_your_name_menu_restart)

        def enter_your_name_menu_go_to_main_menu():
            self.go_to_main_menu = True

        go_to_main_menu_button = Button(x_pos=self.screen_width // 3, y_pos=2 * self.screen_height // 3, width=95,
                                        height=60,
                                        text='Exit',
                                        text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                        handle_event=enter_your_name_menu_go_to_main_menu)

        input_box = Inputbox(self.screen_width // 3, self.screen_height // 3, 140, 60)

        self.buttons_list.extend([restart_button, go_to_main_menu_button])
        self.input_box_list.extend([input_box])

    def enter_your_name_menu_events(self, new_score):
        """Считывает действия пользователя в меню ввода имени"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for input_box in self.input_box_list:
                input_box.handle_event(event, new_score)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons_list:
                    if self.button_collision(button):
                        button.handle_event()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_ESCAPE:
                    self.go_to_main_menu = True

    def run_enter_your_name_menu(self, new_score):
        """Считывает действия пользователя и отрисовывает всё меню ввода имени"""
        self.enter_your_name_menu_events(new_score)
        self.update()
        self.draw_entities(self.main_screen)

        self.main_screen.blit(self.enter_your_name_menu_window, (self.screen_width // 6, self.screen_height // 6))
        self.main_screen.blit(self.logo_surface, (self.screen_width // 6 + 20, self.screen_height // 6 + 10))

        pygame.display.update()
