import pygame
import sys

from button import Button

pygame.init()

sys.path.append('../python_project_1')


def records_menu_events(main_menu):
    """Считывает действия пользователя в меню рекордов"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.exit_button.button.collidepoint(event.pos):
                main_menu.exit = True


class Main:
    """Логика меню рекордов. Отвечает за взаимодействие с кнопками меню рекордов"""

    def __init__(self, screen_width, screen_height):
        self.run = False
        self.exit = False

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.button_text_color = (255, 255, 255)
        self.unpressed_button_bg_color = (110, 110, 110)
        self.pressed_button_bg_color = (180, 180, 180)

        self.exit_button = Button(x_pos=0, y_pos=0, height=60, width=95,
                                  text='Exit',
                                  text_color=self.button_text_color, bg_color=self.unpressed_button_bg_color)

    def update(self):
        """Проверка наведения курсора мыши на кнопки меню рекордов"""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.button_collision(self.exit_button, mouse_pos_x, mouse_pos_y)

    def draw_entities(self, screen):
        """Отрисовка кнопок главного меню"""
        self.exit_button.draw_button(screen)

    def button_collision(self, button, mouse_pos_x, mouse_pos_y):
        """Проверка наведения мыши на одну конкретную кнопку меню рекордов"""
        if button.button.collidepoint(mouse_pos_x, mouse_pos_y):
            button.bg_color = self.pressed_button_bg_color
            return
        else:
            button.bg_color = self.unpressed_button_bg_color

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



class RecordsMenu:
    """Класс меню рекордов. Инициализирует всё меню рекордов и обеспечивает его функционирование"""

    def __init__(self):
        self.screen_height = 640
        self.screen_width = 640
        self.records_menu_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake")
        self.screen_color = (114, 77, 163)

        logo_font = pygame.font.SysFont('Georgia', 60, bold=True)
        logo_color = (32, 249, 7)
        self.logo_surface = logo_font.render('Top 10 scores:', True, logo_color)

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.records_menu = Main(self.screen_width, self.screen_height)

    def run_records_menu(self):
        """Считывает действия пользователя и отрисовывает всё меню рекордов"""
        records_menu_events(self.records_menu)
        self.records_menu.update()
        self.records_menu_screen.fill(self.screen_color)
        self.records_menu.draw_entities(self.records_menu_screen)
        self.records_menu.draw_scores(self.records_menu_screen)
        self.records_menu_screen.blit(self.logo_surface, (self.screen_width // 6, 10))
        pygame.display.update()
        self.clock.tick(self.FPS)
