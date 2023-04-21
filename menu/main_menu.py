import pygame
import sys

from menu.default_menu import DefaultMenu
from menu.button import Button

pygame.init()


class MainMenu(DefaultMenu):
    """Класс главного меню. Инициализирует всё главное меню и обеспечивает его функционирование"""

    def __init__(self):
        super().__init__(screen_color=(114, 77, 163))
        logo_font = pygame.font.SysFont('Georgia', 80, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Snake', True, logo_color)

        self.run = True
        self.go_to_story_mode = False
        self.go_to_endless_mode = False
        self.go_to_records_menu = False

        def go_to_endless_mode():
            self.go_to_endless_mode = True

        endless_mode_button = Button(x_pos=self.screen_width // 3, y_pos=self.screen_height // 3,
                                     height=60, width=105, text='Play',
                                     text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                     handle_event=go_to_endless_mode)

        def go_to_records_menu():
            self.go_to_records_menu = True

        records_button = Button(x_pos=self.screen_width // 3, y_pos=self.screen_height // 2,
                                height=60, width=180, text='Records',
                                text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                handle_event=go_to_records_menu)

        def exit_menu():
            pygame.quit()
            sys.exit()

        exit_button = Button(x_pos=self.screen_width // 3, y_pos=2 * self.screen_height // 3,
                             height=60, width=95, text='Exit',
                             text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                             handle_event=exit_menu)

        self.buttons_list.extend([endless_mode_button, records_button, exit_button])

    def main_menu_events(self):
        """Считывает действия пользователя в меню"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons_list:
                    if self.button_collision(button):
                        button.handle_event()

    def run_main_menu(self):
        """Считывает действия пользователя и отрисовывает всё главное меню"""
        self.main_menu_events()
        self.update()
        self.screen.fill(self.screen_color)
        self.draw_entities(self.screen)
        self.screen.blit(self.logo_surface, (self.screen_width // 3, self.screen_height // 12))
        pygame.display.update()
        self.clock.tick(self.FPS)
