import pygame
import sys

from menu.default_menu import DefaultMenu
from menu.button import Button

pygame.init()


class RecordsMenu(DefaultMenu):
    """Логика меню рекордов. Отвечает за взаимодействие с кнопками меню рекордов"""

    def __init__(self):
        super().__init__(screen_color=(114, 77, 163))
        logo_font = pygame.font.SysFont('Georgia', 60, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Top 10 scores:', True, logo_color)

        self.run = False
        self.go_to_main_menu = False

        def go_to_main_menu():
            self.go_to_main_menu = True

        go_to_main_menu_button = Button(x_pos=0, y_pos=0, height=60, width=95, text='Exit',
                                        text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color,
                                        handle_event=go_to_main_menu)

        self.buttons_list.extend([go_to_main_menu_button])

    def draw_scores(self, screen):
        """Отрисовка рекордов"""
        font = pygame.font.SysFont('Georgia', 50, bold=True)
        color = (32, 249, 7)

        input_file = open('../python_project_1/scores.txt', 'r')
        scores = input_file.readlines()[:10]
        input_file.close()
        for (line_index, line) in enumerate(scores):
            divider_index = line.find("#")
            current_name = line[:divider_index]
            current_score = int(line[divider_index + 1:])
            surface = font.render(current_name + ": " + str(current_score), True, color)
            screen.blit(surface, (self.screen_width // 4, 90 + line_index * 52))

    def records_menu_events(self):
        """Считывает действия пользователя в меню рекордов"""
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
                    self.go_to_main_menu = True

    def run_records_menu(self):
        """Считывает действия пользователя и отрисовывает всё меню рекордов"""
        self.records_menu_events()
        self.update()
        self.screen.fill(self.screen_color)
        self.draw_entities(self.screen)
        self.draw_scores(self.screen)
        self.screen.blit(self.logo_surface, (self.screen_width // 6, 10))
        pygame.display.update()
        self.clock.tick(self.FPS)
