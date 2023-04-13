import pygame
import sys
from pygame.math import Vector2

from game.snake import Snake
from game.fruit import Fruit

pygame.init()


def game_events(game, game_screen_update):
    """Считывает действия пользователя в игре"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == game_screen_update:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_ESCAPE:
                game.paused = True


class Main:
    """Логика игры. Отвечает за взаимодействие змеи с фруктом, а также змеи с препятствиями"""

    def __init__(self, cell_size, cell_number):
        self.run = False
        self.paused = False
        self.entering_name = False

        self.cell_size = cell_size
        self.cell_number = cell_number
        self.snake = Snake(cell_size, cell_number)
        self.fruit = Fruit(cell_size, cell_number)
        self.prev_score = 0
        self.last_score = 0
        self.score = 0

    def update(self):
        """Обновление положения змеи и проверка столкновений"""
        if not self.paused or not self.entering_name:
            self.snake.update_snake()
            self.fruit_collision()
            self.obstacle_collision()

    def draw_entities(self, screen):
        """Отрисовка змеи и фрукта"""
        self.snake.draw_snake(screen)
        self.fruit.draw_fruit(screen)

    def fruit_collision(self):
        """Проверка столкновения змеи с фруктом"""
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.respawn()
            self.snake.grow()
            self.score += 10

    def obstacle_collision(self):
        """Проверка столкновения змеи с собой или со стеной"""
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        for segment in self.snake.body[1:]:
            if segment == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        """Перезагрузка игры при проигрыше. Перезагружает змею и обнуляет очки"""
        self.prev_score = self.score
        if self.score >= 50:
            self.entering_name = True
        self.reset()

    def reset(self):
        """Обычная перезагрузка, используется при нажатии кнопки restart в меню паузы"""
        self.snake.respawn()
        self.fruit.respawn()
        self.score = 0


class Game:
    """Класс игры. Инициализирует всю игру и обеспечивает её функционирование"""

    def __init__(self):
        cell_size = 40
        cell_number = 16
        self.game_screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
        pygame.display.set_caption("Snake")
        self.screen_color = (175, 215, 70)

        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.game_screen_update = pygame.USEREVENT
        self.update_frequency = 200
        pygame.time.set_timer(self.game_screen_update, self.update_frequency)

        self.game = Main(cell_size, cell_number)

        self.logo_font = pygame.font.SysFont('Georgia', 40, bold=True)
        self.logo_color = (114, 77, 163)

    def run_game(self):
        """Считывает действия пользователя, а также обновляет и отрисовывает игру"""
        if self.game.score - self.game.last_score >= 25:  # Увеличение скорости передвижения змеи с возрастанием количества очков
            self.game.last_score = self.game.score
            self.update_frequency -= 1
            pygame.time.set_timer(self.game_screen_update, self.update_frequency)

        if not self.game.paused and not self.game.entering_name:
            game_events(self.game, self.game_screen_update)
        self.game_screen.fill(self.screen_color)
        self.game.draw_entities(self.game_screen)

        logo_surface = self.logo_font.render('Your score:' + str(self.game.score), True, self.logo_color)
        self.game_screen.blit(logo_surface, (0, 0))

        if not self.game.paused and not self.game.entering_name:
            pygame.display.update()
        self.clock.tick(self.FPS)
